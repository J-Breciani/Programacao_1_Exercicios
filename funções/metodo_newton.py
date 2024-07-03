def f_quadradoPerfeito(a):
  n = 1
  while (n ** 2 < a):
      n = n + 1
  return n-1

def f_maisProximo(a,x):

  diferenca1 = a - x**2
  diferenca2 = (x+1)**2 - a
  if (diferenca1 < diferenca2):
    return x
  else:
    return (x+1)

def f_newton(a):
  #declaração de variáveis
  x2 = int(0)
  x = int(0)    

  #inicialização:
  qp_anterior = f_quadradoPerfeito(a)
  x = f_maisProximo(a,qp_anterior)
  x2 = x**2

  return (a+x2)/(2*x)

def main():
  #declaração de variáveis
  a = int(0)

  #entrada de dados
  a = int(input())

  #processamento e saída de dados
  while (a >= 0):
      print(f'N={a:.4f} RAIZ={f_newton(a):.6f}')
      a = int(input())

  return 0

if __name__ == "__main__":
  main()  