# Deep Learning



## [전통적인 머신러닝] 을 넘어 딥러닝으로

### 관계도

![](https://blogs.nvidia.co.kr/wp-content/uploads/sites/16/2016/08/postfiles8.naver_.png)

**인공 지능**이 가장 큰 원이고, 그 다음이 **머신 러닝**이며, 현재의 인공지능 붐을 주도하는 **딥 러닝**이 가장 작은 원이라 할 수 있죠.



### 인공지능 기술의 탄생 및 성장



인공 지능이라는 개념은 1956년 미국 다트머스 대학에 있던 존 매카시 교수가 개최한 다트머스 회의에서 처음 등장했으며, 최근 몇 년 사이 폭발적으로 성장하고 있는 중입니다. 특히 2015년 이후 신속하고 강력한 병렬 처리 성능을 제공하는 **GPU**의 도입으로 더욱 가속화되고 있습니다. 갈수록 폭발적으로 늘어나고 있는 저장 용량과 이미지, 텍스트, 매핑 데이터 등 모든 영역의 데이터가 범람하게 된 ‘빅데이터’ 시대의 도래도 이러한 성장세에 큰 영향을 미쳤습니다.



### 딥 러닝 : 완전한 머신 러닝을 실현하는 기술



![](http://www.palnews.co.kr/news/photo/201801/92969_25283_5321.jpg)



초기 머신 러닝 연구자들이 만들어 낸 또 다른 알고리즘인 인공 신경망 (artificial neural network) 에 영감을 준 것은 인간의 뇌가 지닌 생물학적 특성, 특히 뉴런의 연결 구조였습니다. 그러나 물리적으로 근접한 어떤 뉴런이든 상호 연결이 가능한 뇌와는 달리, 인공 신경망은 레이어 연결 및 데이터 전파 방향이 일정합니다.



#### <사람 뇌와 인공신경망의 차이점>

| 구분      | 뇌       | 인공 신경망 |
| --------- | -------- | ----------- |
| 전파 방향 | 상호연결 | 일정        |



![](https://buomsoo-kim.github.io/data/images/2018-04-21/2.jpeg)



**예를 들어**, 이미지를 수많은 타일로 잘라 신경망의 첫 번째 레이어에 입력하면, 그 뉴런들은 데이터를 다음 레이어로 전달하는 과정을 마지막 레이어에서 최종 출력이 생성될 때까지 반복합니다. 그리고 각 뉴런에는 수행하는 작업을 기준으로 입력의 정확도를 나타내는 가중치가 할당되며, 그 후 가중치를 모두 합산해 최종 출력이 결정됩니다.

정지 표지판의 경우, 팔각형 모양, 붉은 색상, 표시 문자, 크기, 움직임 여부 등 그 이미지의 특성을 잘게 잘려 뉴런에서 '검사'되며, 신경망의 임무는 이것이 정지 표지판인지 여부를 식별하는 것입니다. 여기서는 충분한 데이터를 바탕으로 가중치에 따라 결과를 예측하는 **'확률벡터 (Probability Vector)'**가 활용됩니다.

> **확률벡터 (Probability Vector)** : 원소가 모두 확률변수인 벡터

딥 러닝은 인공신경망에서 발전한 형태의 인공 지능으로, 뇌의 뉴런과 유사한 정보 입출력 계층을 활용해 데이터를 학습한다. 그러나 기본적인 신경망조차 굉장한 양의 연산을 필요로 하는 탓에 딥 러닝의 상용화는 초기부터 난관에 부딪혔습니다. 그럼에도 토론토대의 제프리 힌튼(Geoffrey Hinton) 교수 연구팀과 같은 일부 기관에서는 연구를 지속했고, 슈퍼컴퓨터를 기반으로 딥 러닝 개념을 증명하는 알고리즘을 병렬화하는데 성공했습니다. 그리고 병렬 연산에 최적화된 GPU의 등장은 신경망의 연산 속도를 획기적으로 가속하며 진정한 딥 러닝 기반 인공 지능의 등장을 불러왔습니다.

신경망 네트워크는 ‘학습’ 과정에서 수많은 오답을 낼 가능성이 큽니다. 정지 표지판의 예로 돌아가서, 기상 상태, 밤낮의 변화에 관계 없이 항상 정답을 낼 수 있을 정도로 정밀하게 뉴런 입력의 가중치를 조정하려면 수백, 수천, 어쩌면 수백만 개의 이미지를 학습해야 할지도 모르죠. 이 정도 수준의 정확도에 이르러서야 신경망이 정지 표지판을 제대로 학습했다고 볼 수 있습니다.

2012년, 구글과 스탠퍼드대 앤드류 응(Andrew NG) 교수는 1만6,000개의 컴퓨터로 약 10억 개 이상의 신경망으로 이뤄진 ‘심층신경망(Deep Neural Network)’을 구현했습니다. 이를 통해 유튜브에서 이미지 1,000만 개를 뽑아 분석한 뒤, 컴퓨터가 사람과 고양이 사진을 분류하도록 하는데 성공했습니다. 컴퓨터가 영상에 나온 고양이의 형태와 생김새를 인식하고 판단하는 과정을 스스로 학습하게 한 것이죠.

딥 러닝으로 훈련된 시스템의 이미지 인식 능력은 이미 인간을 앞서고 있습니다. 이 밖에도 딥 러닝의 영역에는 혈액의 암세포, MRI 스캔에서의 종양 식별 능력 등이 포함됩니다. 구글의 알파고는 바둑의 기초를 배우고, 자신과 같은 AI를 상대로 반복적으로 대국을 벌이는 과정에서 그 신경망을 더욱 강화해 나갔습니다.



### 딥 러닝으로 밝은 미래를 꿈꾸는 인공 지능



딥 러닝의 등장으로 인해 머신 러닝의 실용성은 강화됐고, 인공 지능의 영역은 확장되었습니다. 딥 러닝은 컴퓨터 시스템을 통해 지원 가능한 모든 방식으로 작업을 세분화합니다. 운전자 없는 자동차, 더 나은 예방 의학, 더 정확한 영화 추천 등 딥 러닝 기반의 기술들은 우리 일상에서 이미 사용되고 있거나, 실용화를 앞두고 있습니다. 딥 러닝은 공상과학에서 등장했던 일반 AI를 실현할 수 있는 잠재력을 지닌 인공 지능의 현재이자, 미래로 평가 받고 있습니다.



### 퍼셉트론(Perceptron)이란?

퍼셉트론은 다수의 신호를 입력으로 받아 하나의 신호를 출력합니다. 전류가 전선을 타고 흐르는 전자를 내보내듯, 퍼셉트론 신호도 흐름을 만들고 정보를 앞으로 전달합니다. 다만, 실제 전류와 달리 퍼셉트론 신호는 '흐른다/안흐른다(1이나 0)'의 두가지 값을 가질 수 있습니다. 



### 퍼셉트론(Perceptron) 구조



![](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F9904E73F5BF4119417)



x1과 x2는 입력 신호, y는 출력 신호, w1과 w2는 가중치를 뜻합니다. (w는 weight의 머리글자죠). 그림의 원을 **뉴런** 혹은 **노드**라고 부릅니다. 입력 신호가 뉴런에 보내질 때는 각각 고유한 **가중치**가 곱해집니다 (w2x1, w1x2). 뉴런에서 보내온 신호의 총합이 정해진 한계를 넘어설 때만 1을 출력합니다 (이를 '뉴런이 활성화한다'라 표현하기도 합니다). 그 한계를 **임계값**이라 하며, θ기호 (theta, 세타)로 나타냅니다.



#### 용어 정리

* **임계치(threshold)** : 어떠한 값이 활성화되기 위한 최소값을 임계치라고 합니다.

* **가중치(weight)** : 퍼셉트론의 학습 목표는 학습 벡터를 두 부류로 선형 분류하기 위한 선형 경계를 찾는 것이다. 가중치는 이러한 선형 경계의 방향성 또는 형태를 나타내는 값입니다.

> **선형 경계 (결정 경계)** : 두 개의 계층을 가지고 있는 통계적인 분류 문제에서, 결정 경계는 기본 벡터공간을 각 클래스에 대하여 하나씩 두 개의 집합으로 나누는 초표면입니다. 분류기는 결정 경계의 한쪽에 있는 모든 점을 한 클래스, 다른 한쪽에 있는 모든 점을 다른 클래스에 속하는 것으로 분류합니다.
>
> > 초평면 : 수학에서, 초평면 (超平面, [영어](https://ko.wikipedia.org/wiki/영어): hyperplane) 은 3차원 공간 속의 평면을 일반화하여 얻는 개념입니다.
>
> 결정 경계는 출력 계층이 모호한 문제 공간의 영역입니다. 만약 결정표면이 초평면이라면, 분류문제는 선형이며 그 계층들은 선형적으로 분리가능합니다.

* **바이어스(bias)** : 선형 경계의 절편을 나타내는 값으로써, 직선의 경우는 y절편을 나타냅니다.
* **net값** : 입력값과 가중치의 곱을 모두 합한 값으로써, 기하학적으로 해석하면 선형 경계의 방정식과 같습니다.
* **활성함수 (activation function)** : 뉴런에서 계산된 net값이 임계치보다 크면 1을 출력하고, 임계치보다 작은 경우에는 0을 출력하는 함수입니다. 이 정의는 단층 퍼셉트론에서만 유효하며, 다층 퍼셉트론에서는 다른 형태의 활성함수를 이용합니다.



퍼셉트론의 동작 원리는 이게 다입니다! 이상을 수식으로 나타내면 다음과 같습니다.

![](https://3.bp.blogspot.com/-KZwkpSMMzjE/Wn7aMLWNUJI/AAAAAAAAACY/mpqHZIMgI8oa_m0AWH2AINqn065qSjvlwCLcBGAs/s1600/step%2Bfunction.PNG)



퍼셉트론의 전체구조를 좀 더 들여다보면 다음과 같은 구조가 나타납니다.



![](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F996B973359E073B340)



각 뉴런에는 입력신호를 가공하여 출력을 도출하기 위해서 활성화 함수 (activation function)가 역할을 하는데, 활성화 함수에는 계단 함수, 시그모이드 함수, Rectified Linear Unit 함수 등이 있습니다. 



#### Single-Layer Perceptron Structure

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F261AC64E56C2D0E7241637)

> x는 입력 벡터의 값을 나타내고 w는 가중치를 나타냅니다. 바이어스 입력값은 x0, 바이어스 기울기는 w0으로 표기했으며 f는 활성함수를 나타냅니다.



#### 과정

두가지 연산을 적용하여 출력값을 계산한다.

* 넘겨져 온 데이터와 θ들의 Linear combination
* Activation function

**1) 넘겨져 온 데이터와 θ들의 Linear combination 을 계산 (합 & 곱)**

> 이전 Layer 혹은 외부로부터 넘겨져 온 데이터와 각 θ 사이의 Linear Combination
>
> > Linear combination : In mathematics, a linear combination is an expression constructed from a set of terms by multiplying each term by a constant and adding the results (e.g. a linear combination of x and y would be any expression of the form ax + by, where a and b are constants.). The concept of linear combinations is central to linear algebra and related fields of mathematics. Most of this article deals with linear combinations in the context of a vector space over a field, with some generalizations given at the end of the article.

**2) 선형결합의 결과에 Activation function (활성화 함수) 을 적용**

> Linear combination 의 결과값이 Non-linear Function을 거치게 하여 최종 출력값을 계산



### 단순한 논리 회로

#### 1. AND 게이트

AND 게이트는 입력이 둘이고 출력은 하나입니다. 입력 신호와 출력 신호의 대응 표를 **진리표**라고 합니다. 다음은 AND 게이트의 진리표인데, 두 입력이 모두 1일 때만 1을 출력하고, 그 외에는 0을 출력합니다.

![](http://pds26.egloos.com/pds/201303/28/12/f0037512_5153b6eac6895.jpg)

가령 (w1, w2, θ)가 (0.5, 0.5, 0.7)일 때, 또 (0.5, 0.5, 0.8)이나 (1.0, 1.0, 1.0) 때 모두 AND 게이트의 조건을 만족합니다. 매개변수를 이렇게 설정하면, x1과 x2 모두가 1일 때만 가중 신호의 총합이 주어진 임계값을 웃돌게 됩니다. 

#### 2. NAND 게이트와 OR 게이트

NAND는 Not AND를 의미하며, 그 동작은 AND 게이트의 출력을 뒤집은 것이 됩니다.

![](http://thumbnail.egloos.net/460x0/http://pds26.egloos.com/pds/201303/28/12/f0037512_5153c1b1ac4cc.jpg)

NAND 게이트를 표현하려면 예를 들어 (w1, w2, θ) = (-0.5, -0.5, -0.7) 조합이 있습니다. 사실 AND 게이트를 구현하는 매개변수의 부호를 모두 반전하기만 하면 NAND 게이트가 됩니다.

OR 게이트는 입력 신호 중 하나 이상이 1이면 출력이 1이 되는 논리 회로입니다.

![](C:\Users\mseok\TIL\image\OR_gate.jpg)

## Keras Model, with transfer learning

A neural network classifier is made of several layers of neurons. For image classification these can be **dense** or, more frequently, **convolutional** layers. They are typically activated with relu activation function. The last layer uses as many neurons as there are classes and is activated with *softmax*.

> **Softmax Function**: 입력받은 값을 출력으로 0~1사이의 값으로 모두 정규화하며 출력 값들의 총합은 항상 1이 되는 특성을 가진 함수이다. 분류하고 싶은 클래스의 수 만큼 출력으로 구성한다. 가장 큰 출력 값을 부여받은 클래스가 확률이 가장 높은 것으로 이용된다. 그러나, 소프트맥스 결과값이 [ 0.4, 0.3, 0.2, 0.1 ]으로 나와 1등한 0.4와 [ 0.7, 0.1, 0.1, 0.1 ]으로 나와 1등한 0.7은 다를 것이므로 그 정도에 따라 추가 판단하기도 한다.

For classification, cross-entropy is the most commonly used loss function, comparing the one-hot encoded labels ( i.e. correct answers ) with probabilities predicted by the neural network. To minimize the loss, it is best to choose an optimizer with momentum, for example AdamOptimizer and train on batches of training images and labels.



```python
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=[192, 192, 3]),
    tf.keras.layers.Dense(500, activation="relu"),
    tf.keras.layers.Dense(50, activation="relu"),
    tf.keras.layers.Dense(5, activation='softmax') # classifying into 5 classes
])

# this configures the training of the model. Keras calls it "compiling" the model.
model.compile(
  optimizer='adam',
  loss= 'categorical_crossentropy',
  metrics=['accuracy']) # % of correct answers

# train the model
model.fit(dataset, ... )
```



### Dense neural network

This is the simplest neural network for classifying images. It is made of "neurons" arranged in layers. The first layer processes input data and feeds its outputs into other layers. It is called "dense" because each neuron is connected to all the neurons in the previous layer.

![](https://lh6.googleusercontent.com/eZH8QIod6Ox7rXZHxuFdn8sO1xKwvQijFhbvDJvA3IInuHoLns_jhSnu3IC7Z_zun4hoY0sc7qMtRoo0QoHuvV3b34HmAisP44O2isb0MjXA2G7KcDJAM6zbpsDyiwESvtq33rsw)

You can feed an image into such a network by flattening the RGB values of all of its pixels into a long vector and using it as inputs. **It is not the best technique for image recognition but we will improve on it later.**



## 관련 사이트

[NVIDIA 공식 블로그](https://blogs.nvidia.co.kr/2016/08/03/difference_ai_learning_machinelearning/)

