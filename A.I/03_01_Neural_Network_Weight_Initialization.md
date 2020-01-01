# Neural Network - Weight Initialization

<img src="C:\Users\mseok\TIL\images\NN.png" alt="Neural Network" style="zoom:50%;" />

이번 글에서는 가중치 초기화 방법들에 대해서 살펴보겠습니다.



## 가중치 초기화의 중요성

처음 weight 값들을 평균이 0이며 표준편차가 1인 표준 정규분포를 이용해 초기화 했을 경우에 Sigmoid 함수의 출력값이 0과 1에 치우치는 현상이 발생합니다. 이 현상이 왜 문제인지 알기 위해 Sigmoid 함수를 살펴보겠습니다.



![Sigmoid Function](C:\Users\mseok\TIL\images\sigmoid_deviation.png)



출력값이 0과 1에 치우치면 Gradient는 0에 가까운 값을 갖게 되고 이는 Gradient Vanishing 현상의 원인이 됩니다. 따라서 Activation Function을 변경시키는 것 뿐 아니라 가중치를 적절하게 초기화 하는 것을 통해서도 Gradient Vanishing 현상을 어느정도 해소할 수 있습니다.



## 표준편차를 줄이는 방법을 통한 개선

weight의 값들이 0에서 멀수록, 즉 표준편차가 클 수록 Sigmoid Function을 사용할 때 0과 1에 치우치는 현상이 발생할 것입니다. 이를 해결하기 위한 방법 중 하나로 표준편차가 작은 정규분포 형태로 weight 들을 초기화 하는 방법이 있습니다.



![Standardized_layers](C:\Users\mseok\TIL\images\Standardized_layers.png)



 

표준편차를 0.01로 하는 정규분포 형태로 초기화 했을 때 출력값들을 나타낸 그래프입니다. 표준편차 1일 때와 달리 0.5 중심으로 모여 있는 것을 확인할 수 있습니다. 이렇게 구성되어 있다면 표준편차가 1일 때보다 의미있는 ( 0이 아닌 ) Gradient 값들을 갖게 될 것이고 Gradient Vanishing 현상을 완화할 수 있습니다.

**그러나, Gradient Vanishing 현상을 완화하는 발전된 방법이 있다.**



## Xavier Initialization

Gradient Vanishing 현상을 완화하기 위해서 가중치를 초기화 할 때 Sigmoid와 같은 S자 함수의 경우 가장 중요한 것은 출력값들이 표준 정규 분포 형태를 갖게 하는 것입니다. 출력값들이 표준 정규 분포 형태를 갖게 되어야 안정적으로 학습이 가능하기 때문입니다.

**Xavier Initialization** 혹은 **Glorot Initialization**라고도 불리는 초기화 방법은 이전 노드와 다음 노드의 개수에 의존하는 방법이다. Uniform분포를 따르는 방법과 Normal분포를 따르는 두가지 방법이 사용된다.

Xavier함수는 비선형함수(ex. sigmoid, tahn)에서 효과적인 결과를 보여준다. 하지만 ReLU함수에서 사용 시 출력 값이 0으로 수렴하게 되는 현상을 확인 할 수 있다. 따라서 ReLU함수에서는 또 다른 초기화 방법을 사용해야 한다.



## He Initialization

ReLU를 활성화 함수로 사용 시 Xavier 초기값 설정이 비효율적인 결과를 보이는 것을 확인했는데, 이런 경우 초기화 방법을 **He Initialization**이라고 한다. 이 방법 또한 정규분포와 균등분포 두가지 방법이 사용된다.

##### 참고 : https://gomguard.tistory.com/184

