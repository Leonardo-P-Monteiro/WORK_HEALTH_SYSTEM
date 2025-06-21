# utils/functions.py

def get_combined_fields(function, selected_activities):
    """
    Função que combina todos os campos M2M e de riscos aplicados de uma 
    Function com suas SpecialActivities selecionadas.
    
    Args:
        function: Instância do modelo Function
        selected_activities: Lista de instâncias de SpecialActivity selecionadas
        
    Returns:
        Dicionário com todos os campos e riscos combinados
    """
    # Lista dos campos ManyToMany diretos (Exames, EPIs, Treinamentos)
    direct_m2m_fields = [
        'trainings', 'epis',
        'exams_admissional', 'exams_periodic', 'exams_dismissal', 
        'exams_return_work', 'exams_change_function'
    ]
    
    # Lista dos 'related_name' dos nossos novos modelos de riscos aplicados
    risk_related_names = [
        'applied_risks_physical',
        'applied_risks_chemical',
        'applied_risks_biological',
        'applied_risks_ergonomic',
        'applied_risks_accident',
    ]

    result = {}
    
    # --- 1. Combina os campos ManyToMany diretos (lógica que você já tinha) ---
    for field_name in direct_m2m_fields:
        # Pega os objetos da função base
        function_objects = getattr(function, field_name).all()
        
        # Usa um dicionário para remover duplicatas por ID
        objects_dict = {obj.id: obj for obj in function_objects}
        
        # Itera sobre as atividades especiais selecionadas
        for activity in selected_activities:
            activity_objects = getattr(activity, field_name).all()
            for obj in activity_objects:
                if obj.id not in objects_dict:
                    objects_dict[obj.id] = obj
        
        result[field_name] = list(objects_dict.values())
    
    # --- 2. Combina os Riscos Aplicados (NOVA LÓGICA) ---
    for related_name in risk_related_names:
        # Pega os riscos aplicados da função base
        # Ex: function.applied_risks_physical.all()
        function_applied_risks = list(getattr(function, related_name).all())
        
        # Pega os riscos aplicados de cada atividade especial e junta na mesma lista
        # Ex: activity.applied_risks_physical.all()
        for activity in selected_activities:
            activity_applied_risks = getattr(activity, related_name).all()
            function_applied_risks.extend(activity_applied_risks)

        # Adiciona a lista combinada e final ao resultado.
        # Não estamos removendo duplicatas aqui, pois um risco aplicado à função
        # e o mesmo risco aplicado a uma atividade são registros distintos e importantes.
        result[related_name] = function_applied_risks

    print('get_combined_fields success executed.')
    
    return result