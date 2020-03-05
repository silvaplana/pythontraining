class Toto:
    """Ma classe"""

    def __init__(self, ):
        pass

    def division(self, a, b):
        if a==1:
            raise Exception("a doit etre different de 1")
        return a / b


if __name__ == "__main__":

    # creation
    print("================ debut ==================")

    t = Toto()

    try:
        t.division(1, 0)
    except ZeroDivisionError as e:
        print("pas divisible par 0:",e)
    except Exception as e:
        print("My excepption:", e)
    finally :
        print("autre")

