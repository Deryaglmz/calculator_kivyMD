
def clearFunc(self):
    self.ids.calculatorResult.text='0'


def button_releaseFunc(self,button):
    prior = self.ids.calculatorResult.text

    if prior == '0':
        self.ids.calculatorResult.text= f'{button}'
    else: 
        self.ids.calculatorResult.text=f'{prior}{button}'

def math_signFunc(self, sign):
    prior = self.ids.calculatorResult.text
    self.ids.calculatorResult.text = f'{prior}{sign}'

def equalsFunc(self):
    prior = self.ids.calculatorResult.text
    try:
        answer = eval(prior)
        self.ids.calculatorResult.text = str(answer)
    except:
        self.ids.calculatorResult.text = "Error"