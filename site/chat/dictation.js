/* Root & Ritual Chat voice input: the browser's own speech recognition only (no outside AI service).
   Voice input never submits a message; the words land in the draft for the visitor to review. */
(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const mic=$('dictate'), input=$('messageInput'), note=$('dictationStatus');
  const Recognition=window.SpeechRecognition||window.webkitSpeechRecognition;
  let active=false, stage='idle', generation=0, engine=null, timer=null, limit=null, prefix='', suffix='', selection='', spoken='';
  const join=(a,b,c)=>a+(a&&!/\s$/.test(a)&&b?' ':'')+b+(c&&!/^\s/.test(c)&&b?' ':'')+c;
  function controls(){
    const label=stage==='listening'?'Stop voice input':active?'Cancel voice input':'Start voice input';
    mic.setAttribute('aria-label',label);mic.setAttribute('title',label);mic.setAttribute('aria-pressed',String(active));
    input.readOnly=active;$('send').disabled=active;$('dictationLanguage').disabled=active;
  }
  function message(text){note.textContent=text;}
  function finish(text){clearTimeout(timer);clearTimeout(limit);timer=limit=null;active=false;stage='idle';engine=null;controls();if(text)message(text);}
  function draft(){input.value=spoken?join(prefix,spoken,suffix):prefix+selection+suffix;}
  function cancel(){
    generation++;const old=engine;engine=null;
    if(old){old.onresult=old.onend=old.onerror=old.onstart=null;try{old.abort();}catch{}}
    finish('Voice input stopped. Your draft is preserved.');
  }
  window.rootRitualDictation={isActive:()=>active,cancel};
  function snapshot(){const a=input.selectionStart??input.value.length,b=input.selectionEnd??a;prefix=input.value.slice(0,a);suffix=input.value.slice(b);selection=input.value.slice(a,b);spoken='';}
  function start(token){
    try{
      engine=new Recognition();const session=engine;
      session.lang=$('dictationLanguage').value;session.continuous=true;session.interimResults=true;session.maxAlternatives=1;
      stage='starting';controls();message('Allow microphone access if prompted…');
      timer=setTimeout(()=>{if(token!==generation)return;cancel();message('Speech recognition did not start. Check the microphone permission for this site, or use your keyboard’s microphone.');},15000);
      session.onstart=()=>{if(token!==generation)return;clearTimeout(timer);stage='listening';controls();message('Listening… Tap the microphone again to finish.');};
      session.onresult=event=>{
        if(token!==generation)return;
        const phrases=[];for(let i=0;i<event.results.length;i++)phrases.push(event.results[i][0].transcript.trim());
        spoken=phrases.filter(Boolean).join(' ');draft();message('Listening… Words appear in your draft. Tap the microphone to finish.');
      };
      session.onend=()=>{if(token!==generation)return;generation++;draft();finish(spoken?'Voice input finished. Review your message, then Send.':'No speech captured. Check your microphone and try again.');};
      session.onerror=event=>{
        if(token!==generation)return;
        const reasons={'not-allowed':'Microphone permission was denied. Allow it in the browser’s site settings, then try again.','service-not-allowed':'This browser’s speech service is blocked. Use your keyboard’s microphone instead.','audio-capture':'No microphone was found. Connect or select one, then try again.','network':'The browser’s speech service could not be reached. Use your keyboard’s microphone instead.','no-speech':'No speech was heard. Tap the microphone and try again.'};
        cancel();message(reasons[event.error]||'Speech recognition failed. Try again, or use your keyboard’s microphone.');
      };
      session.start();
      limit=setTimeout(()=>{if(token===generation&&engine)stop();},180000);
    }catch{cancel();message('Could not start voice input. Check the microphone permission for this site.');}
  }
  function stop(){
    if(!engine)return;stage='stopping';controls();message('Finishing voice input…');
    try{engine.stop();}catch{cancel();return;}
    clearTimeout(timer);timer=setTimeout(()=>{draft();cancel();message('Voice input finished. Review the captured text before sending.');},2500);
  }
  mic.addEventListener('click',()=>{
    if(active){if(stage==='listening')stop();else cancel();return;}
    if(!Recognition){message('Voice input is not available in this browser. Use your keyboard’s microphone instead.');return;}
    if(window.isSecureContext===false){message('Voice input needs a secure (https) page.');return;}
    window.speechSynthesis?.cancel();snapshot();active=true;const token=++generation;controls();start(token);
  });
  $('composer').addEventListener('submit',e=>{if(active){e.preventDefault();e.stopImmediatePropagation();message('Finish voice input and review your draft before sending.');}},true);
  input.addEventListener('keydown',e=>{if(active&&e.key==='Enter'){e.preventDefault();e.stopImmediatePropagation();}if(active&&e.key==='Escape')mic.click();},true);
  $('newChat').addEventListener('click',()=>{if(active)cancel();},true);
  document.querySelector('.messages').addEventListener('click',e=>{if(active&&e.target.closest('button')?.textContent==='Read aloud')cancel();},true);
  document.addEventListener('visibilitychange',()=>{if(document.hidden&&active)cancel();});
  window.addEventListener('pagehide',cancel);
})();
