# automate_download_youtube_videos
1.scrape the urls
```
var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);
window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title-link"){console.log(v.href)}});
```
2.easy script to download youtube videos by python </br>
```
python download_videos.py
```
