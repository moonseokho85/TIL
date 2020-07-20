// 로그인 라우팅 함수 - 데이터베이스의 정보와 비교
var login = function (req, res) {
    console.log("user 모듈 안에 있는 login 호출됨");

    var paramId = req.body.id || req.query.id;
    var paramPassword = req.body.password || req.query.password;
    console.log('요청 파라미터: ' + paramId + ', ' + paramPassword);
    
    var database = req.app.get('database');
    if (database.db) {
        authUser(database, paramId, paramPassword, function (err, docs) {
            if (err) { throw err; }

            if (docs) {
                console.dir(docs);
                
                res.writeHead(200, { 'Content-Type': 'text/html;charset=utf8' })

                var context = {
                    userid: paramId,
                    username: docs[0].name
                }
                
                req.app.render('login_success', context, function (err, html) {
                    if (err) {
                        console.error('뷰 렌더링 중 에러 발생: ' + err.stack);
                        console.log('에러 발생');

                        res.writeHead(200, { 'Content-Type': 'text/html;charset=utf8' })
                        res.write('<h1>뷰 렌더링 중 에러 발생</h1>')
                        res.write('<br><p>' + err.stack + '</p>');
                        res.end();

                        return;
                    }
                    console.log('rendered: ' + html);
                    res.end(html);
                });
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
};

var adduser = function (req, res) {
    console.log('user 모듈 안에 있는 adduser 호출됨');

    var paramId = req.body.id || req.query.id;
    var paramPassword = req.body.password || req.query.password;
    var paramName = req.body.name || req.query.name;

    console.log('요청 파라미터: ' + paramId + ', ' + paramPassword + ', ' + paramName);
    
    // 데이터베이스 객체가 초기화된 경우, addUser 함수 호출하여 사용자 추가
    var database = req.app.get('database')
    if (database.db) {
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
};

// 사용자 리스트 함수
var listuser = function (req, res) {
    console.log('user 모듈 안에 있는 listuser 호출됨.');
    
    // 데이터베이스 객체가 초기화된 경우, 모델 객체의 findAll 메소드 호출
    var database = req.app.get('database')
    if (database.db) {
        // 1. 모든 사용자 검색
        database.UserModel.findAll(function (err, results) {

            console.log('findAll function executing...')

            // 오류가 발생했을 때 클라이언트로 오류 전송
            if (err) {
                console.error('사용자 리스트 조회 중 오류 발생: ' + err.stack);

                res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
                res.write('<h2>사용자 리스트 조회 중 오류 발생</h2>');
                res.write('<p>' + err.stack + '</p>');
                res.end();

                return;
            }

            if (results) {
                console.dir(results);

                var context = {
                    results: results
                }

                req.app.render('listuser', context, function (err, html) {
                    if (err) {
                        console.error('뷰 렌더링 중 에러 발생: ' + err.stack);
                        console.log('에러 발생');

                        res.writeHead(200, { 'Content-Type': 'text/html;charset=utf8' })
                        res.write('<h1>뷰 렌더링 중 에러 발생</h1>')
                        res.write('<br><p>' + err.stack + '</p>');
                        res.end();

                        return;
                    }
                    res.writeHead(200, { 'Content-Type': 'text/html;charset=utf8' })
                    res.end(html);
                });
            } else {
                res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
                res.write('<h2>사용자 리스트 조회 실패</h2>');
                res.end();
            }
        });
    } else {
        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>데이터베이스 연결 실패</h2>');
        res.end();
    }
};

// 사용자를 인증하는 함수
var authUser = function (db, id, password, callback) {
    console.log('authUser 호출됨');

    // 1. 아이디를 사용해 검색
    db.UserModel.findById(id, function (err, results) {
        if (err) {
            callback(err, null);
            return;
        }

        console.log('아이디 [%s]로 사용자 검색 결과', id);
        console.dir(results);

        if (results.length > 0) {
            console.log("아이디와 일치하는 사용자 찾음.");

            // 2. 비밀번호 확인: 모델 인스턴스를 개체로 만들고 authenticate() 메소드 호출
            var user = new db.UserModel({ id: id });
            var authenticated = user.authenticate(password, results[0]._doc.salt, results[0]._doc.hashed_password);

            if (authenticated) {
                console.log('비밀번호 일치함');
                callback(null, results)
            } else {
                console.log("비밀번호 일치하지 않음.");
                callback(null, null);
            }
        } else {
            console.log("아이디와 일치하는 사용자를 찾지 못함.");
            callback(null, null);
        }
    });
}

// 사용자를 추가하는 함수
var addUser = function (db, id, password, name, callback) {
    console.log('addUser 호출됨');

    // UserModel 인스턴스 생성
    var user = new db.UserModel({ "id": id, "password": password, "name": name });

    // save()로 저장
    user.save(function (err) {
        if (err) {
            callback(err, null);
            return;
        }

        console.log("사용자 데이터 추가함.");
        callback(null, user);
    });
}

module.exports.login = login;
module.exports.adduser = adduser;
module.exports.listuser = listuser;