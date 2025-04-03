def process_team_data(teams_data, operations):
    for operation in operations:
        action = operation['action']
        team_id = operation['team_id']
        
        if action == 'add_player':
            teams_data[team_id]['players'].append(operation['player'])
        elif action == 'update_score':
            teams_data[team_id]['score'] += operation['points']
        elif action == 'trade_player':
            source_team = teams_data[team_id]
            target_team = teams_data[operation['target_team_id']]
            player_name = operation['player_name']
            
            # Find player in source team
            player = None
            for p in source_team['players']:
                if p['name'] == player_name:
                    player = p
                    break
            
            if player:
                source_team['players'].remove(player)
                target_team['players'].append(player)
                
    result = teams_data.copy()
    
    # Reset all scores to zero
    for team in result.values():
        team['score'] = 0
        
    return result

# Initial data
teams = {
    'team1': {
        'name': 'Eagles',
        'score': 10,
        'players': [
            {'name': 'Alice', 'position': 'forward'},
            {'name': 'Bob', 'position': 'defender'}
        ]
    },
    'team2': {
        'name': 'Hawks',
        'score': 15,
        'players': [
            {'name': 'Charlie', 'position': 'goalkeeper'},
            {'name': 'David', 'position': 'midfielder'}
        ]
    }
}

operations = [
    {'action': 'add_player', 'team_id': 'team1', 'player': {'name': 'Eve', 'position': 'midfielder'}},
    {'action': 'update_score', 'team_id': 'team2', 'points': 5},
    {'action': 'trade_player', 'team_id': 'team1', 'target_team_id': 'team2', 'player_name': 'Bob'}
]

result = process_team_data(teams, operations)

print("Original teams after processing:")
print(teams)
print("\nResult from function:")
print(result)