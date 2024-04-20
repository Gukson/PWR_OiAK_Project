class ClassicMultiplication:
    def __add(self, a, b):
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        result = ''
        carry = 0
        for i in range(max_len - 1, -1, -1):
            if int(a[i]) + int(b[i]) + carry == 0:
                result = '0' + result
                carry = 0
            elif int(a[i]) + int(b[i]) + carry == 1:
                result = '1' + result
                carry = 0
            elif int(a[i]) + int(b[i]) + carry == 2:
                result = '0' + result
                carry = 1
            elif int(a[i]) + int(b[i]) + carry == 3:
                result = '1' + result
                carry = 1
        if carry == 1:
            result = '1' + result
        return result

    #metoda zwykła bez uzupełnień
    def multiply(self, a, b):
        tmp = 0
        result = ''
        for i in range(len(b)-1, -1, -1):
            if b[i] == '1':
                temp = ''
                for j in range(0, tmp): temp += '0'
                result = self.__add(result, '1' + a + temp)
            if b[i] == '0':
                temp = ''
                for j in range(0, len(a) + tmp): temp += '0'
                result = self.__add(result, '1' + temp)
            tmp += 1
        temp = ''
        for j in range(len(result)): temp += '0'
        result = self.__add(result, '1' + temp[:len(result)-len(a)] + '1' + temp[len(result)-len(a):])
        while len(result) > len(a) + len(b) or result[0] == '0':
            result = result[1:]
        print(result)