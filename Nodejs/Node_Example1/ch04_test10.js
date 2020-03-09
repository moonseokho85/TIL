// Buffer 객체의 기능을 확인하기 위해 만든 코드

// 버퍼 객체를 크기만 지정하여 만든 후 문자열을 씁니다.
var output = '안녕 1!';
var buffer1 = new Buffer(10);
var len = buffer1.write(output, 'utf-8');