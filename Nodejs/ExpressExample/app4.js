var express = require('express');
var http = require('http');

var app = express();

app.use(function(req, res, next){
    console.log('첫 번째 미들웨어에서 요청을 처리함.');

    // (Optional)
    res.send({name: '소녀시대', age: 20}); // send() 메소드는 응답 데이터를 좀 더 간단하게 전송하기 위해 익스프레스에서 추가된 것입니다.
    
    // (Optional)
    // res.status(403).send("Forbidden");

    // res.sendStatus(403);

    next();

});

app.use(function(req, res, next){
    console.log('두 번째 미들웨어에서 요청을 처리함.');
    // console.log('req: ', req)
    // console.log('res: ', res)

    res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
    res.end('<h1>Express 서버에서' + req.user + '응답한 결과입니다.</h1>');
});

http.createServer(app).listen(3000, function(){
    console.log('Express 서버가 3000번 포트에서 시작됨.');
});
