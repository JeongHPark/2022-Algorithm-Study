/*https://taehoung0102.tistory.com/262를 참고

이모티콘마다 모든 할인율을 적용해보면서 가장 조건에 맞는 답을 찾아낸다.
각 이모티콘의 현재 할인율을 저장하는 배열을 만들고 할인율을 적용한 후 계산한다.
*/
class Solution {
    int[] answer = {0,0};
    public int[] solution(int[][] users, int[] emoticons) {
        int[] arr=new int[emoticons.length];//각 이모티콘의 할인율 저장하는 배열

        fill_arr(arr,0,users,emoticons);

        return answer;
    }
    public void fill_arr(int[] arr,int start,int[][] users,int[] emoticons){
        //모든 이모티콘에 대해 10~40까지의 모든 할인율 적용하는 함수
        if(start==emoticons.length){ //이모티콘 마다 할인율 적용이 끝나면 계산하기
            cal(arr,users,emoticons);
            return;
        }

        for(int i=10;i<=40;i+=10) {//할인율을 10씩 증가시키면서 적용
            arr[start] = i;
            fill_arr(arr, start + 1, users, emoticons);
        }
    }

    public void cal(int[] arr, int[][] users, int[] emoticons)
    {
        /*
        모든 사용자에 대해 이모티콘 할인율에 따른 매출액을 계산한다.
        모든 사용자에 대한 계산이 끝나면 현재 적용되어 있는 할인율에 대한 결과값과 answer에 저장된 값들을 비교하여 조건에 알맞은 것으로 교체한다.
         */
        int human=0;
        int money=0;

        for (int[] user:users){
            int discount=user[0];
            int money_t=user[1];
            int sum=0;

            for (int i=0; i<emoticons.length; i++)
            {
                if (arr[i]>=discount){//사용자의 할인율보다 높으면
                    sum+=(emoticons[i]/100)*(100-arr[i]);
                }
            }
            if (sum>=money_t){
                human++;
            }
            else{
                money+=sum;
            }
        }

        if (human>answer[0]){
            answer[0]=human;
            answer[1]=money;
        }
        else if (human==answer[0]&&money>answer[1])
        {
            answer[1]=money;
        }
    }
}

