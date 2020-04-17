

module.exports = function (router, passport) {
    console.log('Called user_passport.');

    // ===== 회원가입과 로그인 라우팅 함수 =====//
    router.route('/').get(function (req, res) {
        console.log('/ 패스로 요청됨.');

        res.render('index.ejs');
    })

    router.route('/login').get(function (req, res) {
        console.log('/login 패스로  GET 요청됨.');

        res.render('login.ejs', { message: req.flash('loginMessage') });
    })

    router.route('/login').post(passport.authenticate('local-login', {
        successRedirect: '/profile',
        failureRedirect: '/login',
        failureFlash: true
    }));

    router.route('/signup').get(function (req, res) {
        console.log('/signup 패스로 GET 요청됨.');

        res.render('signup.ejs', { message: req.flash('signupMessage') });
    })

    router.route('/signup').post(passport.authenticate('local-signup', {
        successRedirect: '/profile',
        failureRedirect: '/signup',
        failureFlash: true
    }))

    router.route('/profile').get(function (req, res) {
        console.log('requested GET method to /profile path');

        console.log('Object information of req.user');
        console.dir(req.user);

        if (!req.user) {
            console.log('Unauthenticated State.')
            res.redirect('/');
        } else {
            console.log('Authenticated state.');

            if (Array.isArray(req.user)) {
                res.render('profile.ejs', { user: req.user[0]._doc });
            } else {
                res.render('profile.ejs', { user: req.user });
            }
        }
    });

    router.route('/logout').get(function(req, res){
        console.log('requested GET method to /logout path.');

        req.logout();
        res.redirect('/');
    })

    // 패스포트 - 페이스북 인증 라우팅 
    router.route('/auth/facebook').get(passport.authenticate('facebook', { 
        scope : 'email' 
    }));

    // 패스포트 - 페이스북 인증 콜백 라우팅
    router.route('/auth/facebook/callback').get(passport.authenticate('facebook', {
        successRedirect : '/profile',
        failureRedirect : '/'
    }));

}