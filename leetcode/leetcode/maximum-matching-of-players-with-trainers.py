class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left,right,count = 0,0,0
        player_length = len(players)
        trainer_length = len(trainers)
        while left < player_length and right < trainer_length:
            if players[left] <= trainers[right]:
                count += 1
                right += 1
                left += 1
            else:
                right += 1
        
        return count
        