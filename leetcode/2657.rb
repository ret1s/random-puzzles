def find_the_prefix_common_array(a, b)
  n = a.length
  freq = Array.new(n + 1, 0)
  ans = []
  common = 0

  (0...n).each do |i|
    freq[a[i]] += 1
    common += 1 if freq[a[i]] == 2
    freq[b[i]] += 1
    common += 1 if freq[b[i]] == 2
    ans << common
  end

  ans
end