// JavaScript code here

// Hide and Remove all Anvil element
var element = document.getElementById("anvil-header");
if (element) {
  element.style.display = "none";
  element.parentNode.removeChild(element);
  console.log(element)
}
// var s = false; 
// function replaceH_2_WithNewLine() {


// Youtube video play in background
var player;

function onYouTubeIframeAPIReady() {
  player = new YT.Player('video-background', {
    videoId: 'BRfsH5VJwWs',
    playerVars: {

      loop: 1,
      mute: 1,
      controls: 0,
      modestbranding: 1,
      autohide: 1,
      playlist: 'BRfsH5VJwWs'
    },
    events: {
      onReady: onPlayerReady,
      onStateChange: onPlayerStateChange
    }
  });

  // Modify the iframe source to include the desired parameters
  var iframe = document.getElementById('video-background');
  var src = iframe.src;
  iframe.src = src + '?modestbranding=1&rel=0&showinfo=0';
}

function onPlayerReady(event) {
  event. target.playVideo();
  // event.target.setSize(window.innerWidth = 1000, window.innerHeight=1000);
}

function onPlayerStateChange(event) {
  if (event.data === YT.PlayerState.PLAYING) {

    //Remove youtube unwanted elements
    var watchLaterIcon = document.querySelector('ytp-title-link yt-uix-sessionlinkk');
    if (watchLaterIcon) {
      watchLaterIcon.style.display = 'none';
      watchLaterIcon.parentNode.removeChild(watchLaterIcon);
    }
    var watchLater = document.querySelector('ytp-watch-later');
    if (watchLater) {
      watchLater.style.display = 'none';
      watchLater.parentNode.removeChild(watchLaterIcon);
    }
  }
  else
  {
    if (event.data === YT.PlayerState.ENDED) {
      player.playVideo();
    }
  }
}


