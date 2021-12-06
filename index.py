class RomanNumeralConverter:
    """
    Convert between roman numeral symbols to numeric symbols and vice versa
    
    Approach:
    Given a number:
        determine how many thousands are there - return n*M
        deterine how many hubdreds are there - return n*D
        and so on
    """
    def __init__(self, *args):
        super(RomanNumeralConverter, self).__init__(*args)
        self.symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    def get_roman_place_value_by_index(self, index):
        return list(self.symbols.keys())[index]
        
    def get_roman_place_value(self, place_value):
        for k, v in zip(self.symbols.keys(), self.symbols.values()):
            if place_value == v:
                return k
    def get_roman_place_value_index(self, roman_place_value):
        return list(self.symbols.keys()).index(roman_place_value)
    
    def get_roman_value(self, value, place_value):
        repr = ""
        for k, v in zip(reversed(self.symbols.keys()), reversed(self.symbols.values())):
            freq = value // v
            value = value - (freq * v)
            res = k * freq
            repr += res
        return repr
    
    def total_values(self, N):
         rep = reversed(str(N))
         roman_numeral = []
         for i,v in enumerate(rep):
             total_value = int(v)*(10**i)
             place_value = 10**i if i > 0 else 1
             place_value_lower_limit = place_value*10
             upper_change_point = place_value_lower_limit - place_value*2
             mid = place_value_lower_limit//2
             lower_change_point = place_value_lower_limit - place_value*7
             roman_place_value = self.get_roman_place_value(place_value)
             
             print(total_value, place_value)
             
             if int(v) > 0:
                if place_value >= 1000:
                    total_value = total_value // place_value
                    target = (total_value*place_value)//1000
                    print(target, total_value)
                    roman_value = self.get_roman_value(target, place_value)
                    
                else:
                    roman_value = self.get_roman_value(total_value, place_value)
                
                if place_value < 1000:
                    roman_place_value_index = self.get_roman_place_value_index(roman_place_value)
                    value_index = roman_place_value_index
                    mid_value_index = value_index if value_index > 1 else 0
                    upper_roman_place_value = self.get_roman_place_value_by_index(value_index + 2)
                    mid_roman_place_value = self.get_roman_place_value_by_index(mid_value_index+1)

                    if total_value <= place_value_lower_limit and total_value >= upper_change_point:
                        roman_value = roman_place_value * ((place_value_lower_limit - total_value)//place_value) +  upper_roman_place_value
                    elif total_value > lower_change_point and total_value < mid:
                        roman_value = roman_place_value * ((place_value_lower_limit//2 - total_value)//place_value) + mid_roman_place_value
                    
                    
                roman_numeral.append(roman_value)
                
         print("".join(reversed(roman_numeral)))
        
RomanNumeralConverter().total_values(9000)