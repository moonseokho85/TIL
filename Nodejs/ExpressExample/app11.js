// Express 기본 모듈 불러오기
var express = require("express");
var http = require("http");
var path = require("path");

// Express의 미들웨어 불러오기
var bodyParser = require("body-parser");
var static = require("serve-static");

// 오류 핸들러 모듈 사용
var expressErrorHandler = require("express-error-handler");

var cookieParser = require('cookie-parser');

// 익스프레스 객체 생성
var app = express();

// 기본 속성 설정
app.set("port", process.env.PORT || 3000);

// body-parser를 사용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parser를 사용해 application/json 파싱
app.use(bodyParser.json());

app.use("/public", static(path.join(__dirname, "public")));
// OR
// app.use(express.static('public'));

app.use(cookieParser());

// 라우터 객체 참조
var router = express.Router();

// 미들웨어에서 파라미터 확인
router.route('/process/showCookie').get(function(req, res){
    console.log('/process/showCookie 호출됨.');

    res.send(req.cookies)
})

router.route('/process/setUserCookie').get(function(req, res){
    console.log('/process/setUserCookie 호출됨');

    // 쿠키 설정
    res.cookie('user', {
        id: 'mike',
        name: '소녀시대',
        authorized: true
    });

    // redirect로 응답
    res.redirect('/process/showCookie');
});

// 에러 처리
// app.all("*", function (req, res) {
//   res.status(404).send("<h1>ERROR - 페이지를 찾을 수 없습니다.</h1>");
// });

// 라우터 객체를 app 객체에 등록
app.use("/", router);

// 모든 router 처리 끝난 후 404 오류 페이지 처리
var errorHandler = expressErrorHandler({
  static: {
    "404": "./public/404.html",
  },
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

app.use(function (req, res, next) {
  console.log("두 번째 미들웨어에서 요청을 처리함.");
  // console.log('req: ', req)
  // console.log('res: ', res)

  res.writeHead("200", { "Content-Type": "text/html;charset=utf8" });
  res.end("<h1>Express 서버에서" + req.user + "응답한 결과입니다.</h1>");
});

http.createServer(app).listen(3000, function () {
  console.log("Express 서버가 3000번 포트에서 시작됨.");
});
