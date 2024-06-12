import tensorflow as tf
#Вычислительный граф - это граф, в котором каждый узел соответствует операции или переменной .
x1 = tf.constant(1)
x2 = tf.constant(2)

z = tf.add(x1, x2)

#print(z)
#Создадим три узла один для переменной, другой для суммы

a = int(input())
b = int(input())
x1 = tf.constant(a)
x2 = tf.constant(b)
z = tf.add{x1,x2}