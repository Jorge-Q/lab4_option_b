#Name: Jorge Quinonez
#Last Date Modified: November 11, 2018
#Professor: Diego Aguirre
class HTNode(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next

class simple_hash_table(object):
    def __init__(self, table_size):
        self.size = 0 #To keep track of the number of elements
        self.table = [None] * table_size

    def simple_hash(self, word, first_letter): #Hashing method I caame up with
        return (word**first_letter) % len(self.table)

    def get_ascii_value(self, word):
        ascii_sum = 0
        for char in word:
            ascii_sum += ord(char)
        return ascii_sum

    def insert(self, item):
        self.size += 1
        word = self.get_ascii_value(item)
        first_letter = self.get_ascii_value(item[:1])
        position = self.simple_hash(word, first_letter)
        self.table[position] = HTNode(item, self.table[position])


    def average_number_comparisons(self):
        num_nodes = 0
        num_taken = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            if temp is not None:
                num_taken += 1
            while temp is not None:
                num_nodes += 1
                temp = temp.next

        print('The number of taken nodes is:', num_taken)
        print('The number of total nodes is:', num_nodes)
        print('Average is:', num_nodes/num_taken)


    def calculate_load_factor(self):
        answer = self.size / len(self.table) #Load factor is calculated by dividing the number of elements by the size of the table
        print('The load factor is:', answer)


class better_hash_table(object): #Using multiplicative string hash function
    def __init__(self, table_size):
        self.size = 0
        self.table = [None] * table_size

    def good_hash(self, word): #The values were selected as such since they are the best for multiplicative string hashin
        initial = 5381
        for char in word:
            initial = (initial * 33) + self.get_ascii_value(char)
        return initial % len(self.table)

    def get_ascii_value(self, word):
        ascii_sum = 0
        for char in word:
            ascii_sum += ord(char)
        return ascii_sum

    def insert(self, item):
        self.size += 1
        position = self.good_hash(item)
        self.table[position] = HTNode(item, self.table[position])

    def calculate_load_factor(self):
        answer = self.size / len(self.table)
        print('The load factor is:', answer)

    def average_number_comparisons(self):
        num_nodes = 0
        num_taken = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            if temp is not None:
                num_taken += 1
            while temp is not None:
                num_nodes += 1
                temp = temp.next

        print('The number of taken nodes is:', num_taken)
        print('The number of total nodes is:', num_nodes)
        print('Average is:', num_nodes/num_taken)

def main():
        size = int(input('Enter the size of the table you would like to use:'))
        my_table = simple_hash_table(size)
        my_good_table = better_hash_table(size)
        words_file = open('words_copy.txt', 'r')
        for line in words_file: #Inserting elements into the hash tables
            my_table.insert(line)
            my_good_table.insert(line)
        print('****************************************************')
        print('The following actions will be performed with our first hash table, which has a simple hash function:')
        my_table.calculate_load_factor()
        my_table.average_number_comparisons()
        print('****************************************************')
        print('The following actions will be performed with our second hashing function, which has a more complex hash funcion:')
        my_good_table.calculate_load_factor()
        my_good_table.average_number_comparisons()






main()