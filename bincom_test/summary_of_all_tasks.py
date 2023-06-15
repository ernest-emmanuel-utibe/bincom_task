import requests
import re
import psycopg2

# Let get the data from the web page.
url = "http://127.0.0.1:5500/bincom.html"
response = requests.get(url)
data = response.content.decode("utf-8")

# Extract the colors from the data
colors = re.findall(r"(red|blue|green|black|white)", data)

# Calculate the mean color
mean_color = sum(colors) / len(colors)

# Find the most common color
most_common_color = max(colors, key=colors.count)

# Find the median color
median_color = colors[len(colors) // 2]

# Calculate the variance of the colors
variance = sum((color - mean_color) ** 2 for color in colors) / len(colors)

#Calculate the probability that a color is red
probability_that_a_color_is_red = colors.count("red") / len(colors)

# Save the colors and their frequencies in a MySQL database
conn = psycopg2.connect("dbname=Host user=root password=Nathanjames12345_*")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INTEGER)")
for color, frequency in zip(colors, [colors.count(color) for color in colors]):
    cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))
    conn.commit()

# write a recursive searching algorithm to search for a number entered by user in a list of numbers
def recursive_search(number, list):
    if number in list:
        return True
    else:
        for i in range(len(list)):
            if recursive_search(number, list[i]):
                return True
            return False



    # Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10
    def generate_random_number():
        return "".join([str(random.randint(0,1)) for _ range(4)])
    def convert_to_base_10(number):
        result = 0
        for i in range(len(number)):
            result += 2
            result += int(number[i])
        return result


    # Write a program to sum the first 50 fibonacci sequence
    def sum_the_first_50_fibonacci_numbers():
        result = 0
        a, b = 0, 1
        for i in range(50):
            result += a
            a, b = b, a + b
        return result



if __name__ == "__main__":
print("Mean color:", mean_color)
print("Most common color:", most_common_color)
print("Median color:", median_color)
print("Variance:", variance)
print("Probability of red:", probability_that_a_color_is_red)