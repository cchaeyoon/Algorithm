class Solution {
    public int solution(int num1, int num2) {
        // 소수점까지 계산하려면 double로 변환
        double temp = (double) num1 / num2;
        // 결과를 int로 형변환
        int answer = (int) (temp * 1000);
        return answer;
    }
}