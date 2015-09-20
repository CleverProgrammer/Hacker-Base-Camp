=begin

The prime factors of 13195 are 5, 7, 13 and 29. 

What is the largest prime factor of the number 600851475143?

=end

def prime_checker(number)
    return true if number == 2
    (2..number).each do |x|
        if number % x == 0
            return false
        end
            if x == number - 1
                return true
        end
      end
end

def largest_prime_factor(number)
list_1 = []
number.downto(2).each do |x|
  if prime_checker(x) == true && (number % x == 0)
  list_1.push(x)
  puts list_1.first
  end
end
end

=begin
when i call 13195, it puts out 29 four times instead of 1. And it is very \n
slow when i try to run a big number. How the hell do i fix this, qatyler?

=end

