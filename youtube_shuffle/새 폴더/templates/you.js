var request = require('request'),
    cheerio = require('cheerio');

var url = "http://codenamu.org/blog/";

request(url, function (err, res, html) {
    if (!err) {
        var $ = cheerio.load(html);
        
        // 블로그 title 정보 가져오기
        $(".entry-title > a").each(function () {
            var post = {"title": "", "link": "", "summary": "", "category": []};
            var data = $(this);
            
            post["title"] = data.text();
            post["link"] = data.attr("href");
        });
        
        // 블로그 요약 정보 가져오기
        $(".entry-summary > p").each(function (i) {
            // do something
        })
 
        // 블로그 카테고리 가져오기
        $(".entry-categories").each(function (i) {
            $(this).children('a').each(function () {
                // do something
            });
        })
    }
})

// 페이지 안 크롤링하기

var links = document.getElementsByTagName('a'), hrefs = [];
for ( var i = 0 ; i <links.length; i++) { 
hrefs.push(links[i].href);
}


var asdfasdf = document.getElementsByTagName('span'), hrefs2323 = [];
for (var i = 0 ; i <links.length; i++) { 
    hrefs.push(links[i]);
}

//
{/* <div id="textHtml2" name="textHtml2" style="width:400px;height:200px;border:solid 1px gray" contenteditable="true"><p class="MsoNormal"><span lang="EN-US"><a href="https://www.youtube.com/watch?v=-3LugpXuG-g&amp;t=1s"><span style="font-size:10.5pt;line-height:107%;font-family:&quot;Arial&quot;,sans-serif;
background:#F9F9F9">00:01</span></a></span><span class="style-scope"><span lang="EN-US" style="font-size:10.5pt;line-height:107%;font-family:&quot;Arial&quot;,sans-serif;
color:#030303;border:none windowtext 1.0pt;mso-border-alt:none windowtext 0cm;
padding:0cm;background:#F9F9F9"> Stephanie Poetry - I Love You 3000 <o:p></o:p></span></span></p><p class="MsoNormal"><span lang="EN-US"><a href="https://www.youtube.com/watch?v=-3LugpXuG-g&amp;t=210s"><span style="font-size:10.5pt;line-height:107%;font-family:&quot;Arial&quot;,sans-serif;
background:#F9F9F9">03:30</span></a></span><span class="style-scope"><span lang="EN-US" style="font-size:10.5pt;line-height:107%;font-family:&quot;Arial&quot;,sans-serif;
color:#030303;border:none windowtext 1.0pt;mso-border-alt:none windowtext 0cm;
padding:0cm;background:#F9F9F9"> Khai Dreams - Fantasy <o:p></o:p></span></span></p><p class="MsoNormal">



</p><p class="MsoNormal"><span lang="EN-US"><a href="https://www.youtube.com/watch?v=-3LugpXuG-g&amp;t=380s"><span style="font-size:10.5pt;line-height:107%;font-family:&quot;Arial&quot;,sans-serif;
background:#F9F9F9">06:20</span></a></span><span class="style-scope"><span lang="EN-US" style="font-size:10.5pt;line-height:107%;font-family:&quot;Arial&quot;,sans-serif;
color:#030303;border:none windowtext 1.0pt;mso-border-alt:none windowtext 0cm;
padding:0cm;background:#F9F9F9"> </span></span><span class="style-scope"><span style="font-size:10.5pt;line-height:107%;mso-ascii-font-family:Arial;
mso-hansi-font-family:Arial;mso-bidi-font-family:Arial;color:#030303;
border:none windowtext 1.0pt;mso-border-alt:none windowtext 0cm;padding:0cm;
background:#F9F9F9">지다</span></span><span class="style-scope"><span lang="EN-US" style="font-size:10.5pt;line-height:107%;font-family:&quot;Arial&quot;,sans-serif;
color:#030303;border:none windowtext 1.0pt;mso-border-alt:none windowtext 0cm;
padding:0cm;background:#F9F9F9"> (Jida) - Blind (feat. Rachel Lim)&nbsp;<o:p></o:p></span></span></p></div> */}