=begin
Take a list as input
return the sum of the list as output
bonus: take the list as USER_INPUT (but work on it without user input 
first)
=end

list1 = []

puts "Yo Qazi, what's your favorite number?"
num1 = gets.chomp.to_i

puts "Cool! What's the last two digits of your birth year?"
num2 = gets.chomp.to_i

puts 'How many sqaures are there on a chess board?'
num3 = gets.chomp.to_i

list1.push(num1, num2, num3)

list1.inject(:+)


