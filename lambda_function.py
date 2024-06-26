from mitreattack.stix20 import MitreAttackData
mitre_attack_data = MitreAttackData("/tmp/enterprise-attack.json")

def lambda_handler(event, context):
    tactics_map = mitre_attack_data.get_tactics_by_matrix()
    return [{"name": t['name'], "description": t['description'], "id": t['external_references'][0]['external_id']} for t in tactics_map['Enterprise ATT&CK']]