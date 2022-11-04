def calculate_bmi(height, weight):
        print("Height = " + str(height))
        print("Weight = " + str(weight))
    #Add code here to calculate BMI
        bmi =weight/(height*height)
    #Add code here to display calculate BMI
        if bmi >18 and bmi<25:
            print("normal weight")

        elif bmi < 18:
            print("underweight")

        elif bmi > 25:
            print("overweight")

calculate_bmi(weight=1, height=1.73)
