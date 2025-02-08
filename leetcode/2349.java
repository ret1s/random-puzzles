class NumberContainers {

    private Map<Integer, SortedSet<Integer>> numberToIndex; // Stores all current index 
    private Map<Integer, Integer> indexToNumber;

    public NumberContainers() {
        numberToIndex = new HashMap<>();
        indexToNumber = new HashMap<>();
    }
    
    public void change(int index, int number) {
        
        if(indexToNumber.containsKey(index)) { // that means we need to replace 
            int prevNumber = indexToNumber.get(index);
            numberToIndex.get(prevNumber).remove(index);
        }
        indexToNumber.put(index, number);
        SortedSet<Integer> ss = numberToIndex.getOrDefault(number, new TreeSet<>());
        ss.add(index);
        numberToIndex.put(number,ss);
    }
    
    public int find(int number) {
        if(numberToIndex.containsKey(number) && !numberToIndex.get(number).isEmpty())
            return numberToIndex.get(number).first();
        return -1;
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */