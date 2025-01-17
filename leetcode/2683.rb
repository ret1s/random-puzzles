def does_valid_array_exist(derived)
    n = derived.length
    original = Array.new(n, 0)
    
    (0...n-1).each do |i|
        original[i + 1] = original[i] ^ derived[i]
    end
    
    last_derived = original[n-1] ^ original[0]
    return last_derived == derived[n-1]
end