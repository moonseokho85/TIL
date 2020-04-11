// Express 기본 모듈 불러오기
var express = require("express");
var http = require("http");
var path = require("path");

// Express의 미들웨어 불러오기
var bodyParser = require("body-parser");

// 쿠키 모듈 사용
var cookieParser = require("cookie-parser");
var static = require("serve-static");
var errorHandler = require('errorHandler');

// 오류 핸들러 모듈 사용
var expressErrorHandler = require("express-error-handler");

// 세션 모듈 사용
var expressSession = require("express-session");

// 익스프레스 객체 생성
var app = express();

// 기본 속성 설정
app.set('port', process.env.PORT || 3000);

// body-parser를 사용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parser를 사용해 application/json 파싱
app.use(bodyParser.json());

// public 폴더를 static으로 오픈
app.use('/public', static(path.join(__dirname, 'public')));

// cookie-parser 설정
app.use(cookieParser());

// 세션 설정
app.use(expressSession({
    secret: 'my key',
    resave: true,
    saveUninitialized: true
}));

// 몽고디비 모듈 사용
var MongoClient = require('mongodb').MongoClient;

// mongoose 모듈 불러들이기
var mongoose = require('mongoose');

// 데이터베이스 객체를 위한 변수 선언
var database;

// 데이터베이스 스키마 객체를 위한 변수 선언
var UserSchema;

// 데이터베이스 모델 객체를 위한 변수 선언
var UserModel;

// 데이터 베이스에 연결
function connectDB() {
    // 데이터베이스 연결 정보
    var databaseUrl = 'mongodb://localhost:27017/local';

    // // 데이터베이스 연결
    // MongoClient.connect(databaseUrl, { useUnifiedTopology: true }, function (err, db) {
    //     if (err) throw err;

    //     console.log('데이터베이스에 연결되었습니다. : ' + databaseUrl);

    //     // database 변수에 할당
    //     database = db.db('local') // database명을 명시
    // });

    // 데이터 베이스 연결
    console.log('데이터 베이스 연결을 시도합니다.');
    mongoose.Promise = global.Promise;
    mongoose.connect(databaseUrl, { useNewUrlParser: true, useUnifiedTopology: true });
    database = mongoose.connection;

    database.on('error', console.error.bind(console, 'mongoose connection error.'));
    database.on('open', function () {
        console.log('데이터베이스에 연결되었습니다.: ' + databaseUrl);
    })

    // 스키마 정의
    UserSchema = mongoose.Schema({
        id: String,
        name: String,
        password: String
    });
    console.log('UserSchema 정의함');

    // // 별도 추가 정의
    // UserSchema = mongoose.Schema({
    //     id: {type: String, required: true, unique: true},
    //     password: {type: String, required: true},
    //     name: String,
    //     age: Number,
    //     created_at: Date,
    //     updated_at: Date
    // });

    // UserModel 모델 정의
    UserModel = mongoose.model("users", UserSchema);
    console.log("UserModel 정의함.");

    // 연결 끊어졌을 때 5초 후 재연결
    database.on('disconnected', function () {
        console.log('연결이 끊어졌습니다. 5초 후 다시 연결합니다.');
        setInterval(connectDB, 5000);
    });
}

// 사용자를 인증하는 함수
var authUser = function (database, id, password, callback) {
    console.log('authUser 호출됨' + id + ', ' + password);

    // 아이디와 비밀번호를 사용해 검색
    UserModel.find({ "id": id, "password": password }, function (err, results) {
        if (err) {
            callback(err, null);
            return;
        }

        console.log('아이디 [%s], 비밀번호 [%s]로 사용자 검색 결과', id, password);
        console.dir(results);

        if (results.length > 0) {
            console.log("일치하는 사용자 찾음.", id, password);
            callback(null, results);
        } else {
            console.log("일치하는 사용자를 찾지 못함.");
            callback(null, null);
        }
    });
}

// 사용자를 추가하는 함수
var addUser = function (database, id, password, name, callback) {
    console.log('addUser 호출됨: ' + id + ', ' + password);

    // UserModel의 인스턴스 생성
    var user = new UserModel({ "id": id, "password": password, "name": name });

    // save()로 저장
    user.save(function (err) {
        if (err) {
            callback(err, null);
            return;
        }

        console.log("사용자 데이터 추가함.");
        callback(null, user);
    })
}

// 라우터 객체 참조
var router = express.Router();

// 로그인 라우팅 함수 - 데이터베이스의 정보와 비교
router.route('/process/login').post(function (req, res) {
    console.log("/process/login 호출됨");

    var paramId = req.param('id');
    var paramPassword = req.param('password');

    if (database) {
        authUser(database, paramId, paramPassword, function (err, docs) {
            if (err) { throw err; }

            if (docs) {
                console.dir(docs);
                var username = docs[0].name;
                res.writeHead("200", { "Content-Type": "text/html;charset=utf8" });
                res.write("<h1>로그인 성공</h1>");
                res.write("<div><p>사용자 아이디 : " + paramId + "</p></div>");
                res.write("<div><p>사용자 이름 : " + username + "</p></div>");
                res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
                res.end();
            } else {
                res.writeHead("200", { "Content-Type": "text/html;charset=utf8" });
                res.write("<h1>로그인 실패</h1>");
                res.write("<div><p>아이디와 비밀번호를 다시 확인하십시오.</p></div>");
                res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
                res.end();
            }
        });
    } else {
        res.writeHead("200", { "Content-Type": "text/html;charset=utf8" });
        res.write("<h2>데이터베이스 연결 실패</h2>");
        res.write("<div><p>데이터베이스에 연결하지 못했습니다.</p></div>");
        res.end();
    }
});

router.route('/process/adduser').post(function (req, res) {
    console.log('/process/adduser 호출됨');

    var paramId = req.body.id || req.query.id;
    var paramPassword = req.body.password || req.query.password;
    var paramName = req.body.name || req.query.name;

    console.log('요청 파라미터: ' + paramId + ', ' + paramPassword + ', ' + paramName);

    // 데이터베이스 객체가 초기화된 경우, addUser 함수 호출하여 사용자 추가
    if (database) {
        addUser(database, paramId, paramPassword, paramName, function (err, result) {
            if (err) { throw err; }

            // 결과 객체 확인하여 추가된 데이터 있으면 성공 응답 전송
            console.log("result: ", result)
            
            if (result && result.insertedCount > 0) {
                console.dir(result);

                res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
                res.write('<h2>사용자 추가 성공</h2>')
                res.end();
            } else {
                res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
                res.write('<h2>사용자 추가 실패</h2>')
                res.end();
            }
        })
    } else {
        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>데이터베이스 연결 실패</h2>')
        res.end();
    }
})

// 라우터 객체 등록
app.use('/', router);

// 모든 router 처리 끝난 후 404 오류 페이지 처리
var errorHandler = expressErrorHandler({
    static: {
        "404": "./public/404.html",
    },
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

//===== 서버 시작 =====//
http.createServer(app).listen(app.get('port'), function () {
    console.log("서버가 시작되었습니다. 포트 : " + app.get('port'));

    // 데이터베이스 연결
    connectDB();
});