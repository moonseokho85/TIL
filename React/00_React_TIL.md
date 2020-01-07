# React



## creat-react-app으로 프로젝트 생성하기

```shell
$ yarn create react-app hello-react
```

리액트 프로젝트를 만들 때는 이렇게 yarn create react-app <프로젝트 이름> 명령어를 사용합니다.

```shell
$ cd hello-react
$ yarn start # 또는 npm start
```

이렇게 명령어를 입력하면 다음과 같은 화면이 나옵니다.

![react_yarn_start_result](..\images\react_yarn_start_result.png)

그리고 브라우저에서 자동으로 페이지가 띄워질 것입니다. 만약 페이지가 자동으로 열리지 않았다면 브라우저 주소창에 다음 링크를 직접 입력하여 열어 보세요.

* http://localhost:3000

![react-auto-page](..\images\react_auto_page.png)

### 코드 이해하기

#### src/App.js

```react
import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

```react
import React from 'react';
```



이 코드는 리액트를 불러와서 사용할 수 있게 해줍니다. 리액트 프로젝트를 만들 때 node_modules라는 디렉터리도 함께 생성됩니다. 프로젝트 생성 과정에서 node_modules 디렉터리에 react 모듈이 설치됩니다. 그리고 이렇게 import 구문을 통해 리액트를 불러와서 사용할 수 있습니다.

여기서 한 가지 중요한 점이 있습니다. 이렇게 모듈을 불러와서 사용하는 것은 사실 원래 브라우저에는 없던 기능입니다. 브라우저가 아닌 환경에서 자바스크립트를 실행할 수 있게 해 주는 환경인 Node.js에서 지원하는 기능입니다.

이러한 기능을 브라우저에서도 사용하기 위해 번들러(bundler)를 사용합니다. 번들(bundle)은 묶는다는 뜻으로, 파일을 묶듯이 연결하는 것이죠.





![code_bundle](..\images\code_bundle.jpg)





대표적인 번들러로 Webpack, Parcel, Browserify라는 도구들이 있으며, 각 도구마다 특성이 다릅니다. 리액트 프로젝트에서는 주로 **Webpack**을 사용하는 추세입니다. **편의성**과 **확장성**이 다른 도구보다 뛰어나기 때문입니다. 번들러 도구를 사용하면 import(또는 require)로 모듈을 불러왔을 때 불러온 모듈을 모두 합쳐서 하나의 파일을 생성해 줍니다. 또 최적화 과정에서 여러 개의 파일로 분리될 수도 있습니다.



```shell
import logo from './logo.svg';
import './App.css';
```

Webpack을 사용하면 SVG 파일과 CSS 파일도 불러와서 사용할 수 있습니다. 이렇게 파일들을 불러오는 것은 Webpack의 Loader라는 기능이 담당합니다. Webpack의 Loader는 원래 직접 설치하고 설정해야 하지만 React Project를 만들 때 사용했던 create-react-app이 번거로운 작업을 모두 대신해줍니다.



```react
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
```

이 코드는 App이라는 컴포넌트를 만들어 줍니다. function 키워드를 사용하여 컴포넌트를 만들었는데 이러한 컴포넌트를 함수형 컴포넌트라고 부릅니다. 프로젝트에서 컴포넌트를 렌더링하면 함수에서 반환하고 있는 내용을 나타냅니다.

> 랜더링(Rendering) : '보여준다'는 것을 의미합니다.

함수에서 반환 내용을 보면 마치 HTML을 작성한 것 같지만 이 코드는 HTML이 아닙니다. 그렇다고 문자열도 아닙니다. 이런 코드는 JSX라고 부릅니다.



### JSX란?



JSX는 자바스크립트의 확장 문법이며 XML과 매우 비슷하게 생겼습니다. 이런 형식으로 작성한 코드는 브라우저에서 실행되기 전에 코드가 번들링되는 과정에서 바벨을 사용하여 일반 자바스크립트 형태의 코드로 변환됩니다.

#### JSX

```react
function App() {
    return (
    	<div>
        	Hello <b>react</b>
        </div>
    )
}
```

이렇게 작성된 코드는 다음과 같이 변환됩니다.

```jsx
function App() {
    return React.createElement("div", null, "Hello", React.createElement("b", null, "react"))
}
```

만약 컴포넌트를 렌더링 할 때마다 JSX 코드를 작성하는 것이 아니라 위 코드처럼 매번 React.createElement 함수를 사용해야 한다면 매우 불편할 것이다. JSX를 사용하면 매우 편하게 UI를 렌더링 할 수 있습니다.



### JSX의 장점

* 보기 쉽고 익숙하다

>일반 자바스크립트만 사용한 코드와 JSX로 작성한 코드를 한번 비교해 보세요. 몇 초만 보아도 JSX를 사용하는 편이 더 가독성이 높고 작성하기도 쉽다고 느껴집니다. 자바스크립트 요소들을 일일이 만들어야 한다면 불편해서 사용하고 싶지 않을 겁니다.



* 더욱 높은 활용도

>JSX에서는 우리가 알고 있는 div나 span 같은 HTML 태그를 사용할 수 있을 뿐만 아니라, 앞으로 만들 컴포넌트도 JSX 안에서 작성할 수 있습니다. App.js에서는 App 컴포넌트가 만들어져 있습니다. src/index.js 파일을 열어 보면 이 App 컴포넌트를 마치 HTML 태그 쓰듯이 그냥 작성합니다.

#### src/index.js

```react
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

```

##### ReactDOM.render

이 코드는 컴포넌트를 페이지에 렌더링 하는 역할을 하며, react-dom 모듈을 불러와 사용할 수 있습니다. 이 함수의 첫 번째 파라미터에는 페이지에 렌더링할 내용을 JSX 형태로 작성하고, 두 번째 파라미터에는 해당 JSX를 렌더링할 document 내부 요소를 설정합니다. 여기서는 id가 root인 요소 안에 렌더링을 하도록 설정했는데요. 이 요소는 public/index.html 파일을 열어 보면 있습니다.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>
```



### JSX 문법

JSX는 정말 편리한 문법이지만, 올바르게 사용하려면 몇 가지 규칙을 준수해야 합니다.



#### 감싸인 요소

```react
import React from 'react';

function App() {
  return (
    <h1>리액트 안녕!</h1>
    <h2>잘 작동하니?</h2>
  );
}

export default App;
```



이런 형태의 코드는 제대로 작동하지 않습니다. 코드를 저장한 후 웹 브라우저나 개발 서버를 실행했던 터미널을 열어 보시면 다음 오류가 나타날 것입니다.



![react_compile_error](..\images\react_compile_error.png)



요소 여러 개가 부모 요소 하나에 의하여 감싸져 있지 않기 때문에 오류가 발생했습니다. 이 오류는 다음과 같이 코드를 작성하여 해결할 수 있습니다.

##### src/App.js

```react
import React from 'react';

function App() {
  return (
      <div>
    	<h1>리액트 안녕!</h1>
    	<h2>잘 작동하니?</h2>
      </div>
  );
}

export default App;
```

**리액트 컴포넌트에서 요소 여러 개를 왜 하나의 요소로 꼭 감싸 주어야 할까요?**

그것은 Virtual DOM에서 컴포넌트 변화를 감지해 낼 때 효율적으로 비교할 수 있도록 컴포넌트 내부는 하나의 DOM 트리 구조로 이루어져야 한다는 규칙이 있기 때문입니다.

그런데 여기서 꼭 div 요소를 사용하고 싶지 않을 수도 있습니다. 그런 경우에는 리액트 v16 이상 부터 도입된 **Fragment**라는 기능을 사용하면 됩니다.

##### src/App.js

```react
import React, {Fragment} from 'react';

function App() {
  return (
      <Fragment>
    	<h1>리액트 안녕!</h1>
    	<h2>잘 작동하니?</h2>
      </Fragment>
  );
}

export default App;
```

Fragment는 다음과 같은 형태로도 표현할 수 있습니다.

##### src/App.js

```react
import React from 'react';

function App() {
  return (
      <>
    	<h1>리액트 안녕!</h1>
    	<h2>잘 작동하니?</h2>
      </>
  );
}

export default App;
```



#### 자바스크립트 표현

JSX 안에서는 자바스크립트 표현식을 쓸 수 있습니다. 자바스크립트 표현식을 작성하려면 JSX 내부에서 코드를 { }로 감싸면 됩니다. 

```react
import React from "react";

function App() {
  const name = '리액트';
  return (
    <>
      <h1>{name} 안녕!</h1>
      <h2>잘 작동하니?</h2>
    </>
  );
}

export default App;
```



#### ES6의 const와 let

const는 ES6 문법에서 새로 도입되었으며 한번 지정하고 나면 변경이 불가능한 상수를 선언할 때 사용하는 키워드입니다. let은 동적인 값을 담을 수 있는 변수를 선언할 때 사용하는 키워드입니다.

ES6 이전에는 값을 담는 데 var 키워드를 사용했는데요. var 키워드는 scope(해당 값을 사용할 수 있는 코드 영역)가 함수 단위입니다.

```react
function myFunction() {
    var a = "hello";
    if(true) {
        var a = "bye";
        console.log(a); // bye
    }
    console.log(a); // bye
}
myFunction();
```

if 문 바깥에서 var 값을 hello로 선언하고, if 문 내부에서 bye로 설정했습니다. if 문 내부에서 새로 선언했음에도 if 문 밖에서 a를 조회하면 변경된 값이 나타납니다.

이런 결점을 해결해주는 것이 바로 let과 const입니다.

```react
function myFunction() {
    let a = 1;
    if(true) {
        let a = 2;
        
        console.log(a); // 2
    }
    console.log(a); // 1
}
myFunction
```

let과 const는 scope가 함수 단위가 아닌 블록 단위이므로, if 문 내부에서 선언한 a 값은 if 문 밖의 a 값을 변경하지 않습니다.

let과 const 를 사용할 때와 같은 블록 내부에서 중복 선언이 불가능하다는 점에 주의해야 합니다.

```react
let a = 1;
let a = 2; // 오류: Uncaught SyntaxError: Identifier 'a' has already been declared.
```

그리고 const는 한번 선언하면 재설정할 수 없습니다.

```react
const b = 1;
b = 2; // Uncaught TypeError: Assignment to constant variable.
```

그렇다면 어떤 상황에 각 키워드를 사용해야 하는지를 생각해봐야 합니다. 일단 ES6 문법에서 var을 사용할 일은 없습니다. let은 한번 선언한 후 값이 유동적으로 변할 수 있을 때만(예: for 문) 사용하고, const는 한번 설정한 후 변할 일이 없는 값에 사용합니다. 편하게 생각하면 기본적으로 const를 사용하고, 해당 값을 바꾸어야 할 때는 let을 사용하면 되겠습니다.



#### If 문 대신 조건부 연산자

JSX 내부의 자바스크립트 표현식에서 if 문을 사용할 수는 없습니다. 하지만 조건에 따라 다른 내용을 렌더링해야 할 때는 JSX 밖에서 if 문을 사용하여 사전에 값을 설정하거나, {  } 안에 조건부 연산자를 사용하면 됩니다. 조건부 연산자의 또 다른 이름은 삼항 연산자입니다.

##### src/App.js

```react
import React from "react";

function App() {
  const name = '리액트';
  return (
    <>
      {name === '리액트' ? (
        <h1>리액트입니다.</h1>
      ) : (
        <h2>리액트가 아닙니다</h2>
      )}
    </>
  );
}

export default App;

```

이렇게 코드를 작성한 후 저장하면 브라우저에서 '리액트입니다.' 라는 문구를 볼 수 있습니다. 하지만 name 값을 다음과 같이 다른 값으로 바꾸면, '리액트가 아닙니다.'라는 문구가 나타날 것입니다.

#### AND 연산자(&&)를 사용한 조건부 렌더링

개발을 하다 보면 특정 조건을 만족할 때 내용을 보여주고, 만족하지 않을 때 아예 아무것도 렌더링하지 않아야 하는 상황이 올 수 있습니다. 이럴 때도 조건부 연산자를 통해 구현할 수는 있습니다.

**src/App.js**

```react
import React from 'react';

function App() {
    const name = '뤼액트';
    return <div>{name === '리액트' ? <h1>리액트입니다.</h1> : null}</div>
}

export default App;
```

위 코드와 같이 null을 렌더링하면 아무것도 보여 주지 않습니다.

하지만 이것보다 더 짧은 코드로 똑같은 작업을 할 수 있습니다. 다음과 같이 && 연산자를 사용해서 조건부 렌더링을 할 수 있습니다.

**src/App.js**

```react
import React from 'react';

function App(){
    const name = '뤼액트';
    return <div>{name === '리액트' && <h1>리액트입니다.</h1>}</div>;
}

export default App;
```

이렇게 코드를 작성하고 나면 브라우저에 아무것도 나타나지 않을 것입니다. 다시 name 값을 리액트로 설정하면 '리액트입니다.'가 나타날 것입니다.

&& 연산자가 가능한 이유는 false를 렌더링 할 때 null과 똑같이 아무것도 화면에 표시하지 않습니다. 하지만 falsy한 값인 0은 예외적으로 나타납니다.

#### undefined를 렌더링하지 않음

리액트 컴포넌트에서는 함수에서 undefined만 반환하여 렌더링해서는 안됩니다.

**src/App.js**

```react
import React from 'react';
import './App.css';

function App(){
    const name = undefined;
    return name
}

export default App;
```

브라우저를 확인해 보면 다음과 같은 오류를 볼 수 있습니다.

![image](C:\Users\mseok\TIL\React\images\undefined_render_error.png)

어떤 값이 undefined일 수도 있다면, OR(||)를 사용하면 undefined일 때 사용할 값을 지정할 수 있습니다. 고로 오류를 방지할 수 있습니다.

```react
import React from 'react';
import './App.css';

function App(){
    const name = undefined;
    return name || '값이 undefined입니다.'
}

export default App;
```

JSX 내부에서 undefined를 렌더링하는 것도 가능하다.

```react
import React from 'react';
import './App.css';

function App(){
    const name = undefined;
    return <div>{name}</div>;
}

export default App;
```

#### 인라인 스타일링

리액트에서 DOM 요소에 스타일을 적용할 때는 문자열 형태로 넣는 것이 아니라 객체 형태로 넣어야 합니다. 

**src/App.js**

```react
import React from 'react';

function App(){
    const name = '리액트';
    const style = {
        backgroundColor: 'black',
        color:'aqua',
        fontSize: '48px',
        fontWeight: 'bold',
        padding: 16
    };
    return <div style={style}>{name}</div>
}

export default App;
```

지금은 style 객체를 미리 선언하고 div의 style 값으로 지정했지만 바로 style 값을 지정하고 싶다면 안에 넣어주면 됩니다.

