def conjugaison():
    verb = input('Entrez un verbe (premier groupe): ')
    temps = input('Entrez le temps (présent, passé, imparfait ou futur): ')
    mode = input('Entrez le mode (indicatif, conditionnel, imperatif, infinitif, subjunctif): ')
    personne = input('Entrez la personne (1, 2 ou 3): ')
    nombre = input('Entrez le nombre (singulier ou pluriel): ')
    if verb[-2:] == 'er':
        stem = verb[:-2]
    else:
        return 'Verbe non valide'
    if temps == 'présent':
        if mode == 'indicatif':
            endings = ['e', 'es', 'e', 'ons', 'ez', 'ent']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + stem + 'e'
                elif nombre == 'pluriel':
                    return 'Nous ' + stem + 'ons'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + stem + 'es'
                elif nombre == 'pluriel':
                    return 'Vous ' + stem + 'ez'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + stem + 'e'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + stem + 'ent'
        elif mode == 'subjunctif':
            endings = ['e', 'es', 'e', 'ions', 'iez', 'ent']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + stem + 'e'
                elif nombre == 'pluriel':
                    return 'Nous ' + stem + 'ions'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + stem + 'es'
                elif nombre == 'pluriel':
                    return 'Vous ' + stem + 'iez'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + stem + 'e'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + stem + 'ent'
        elif mode == 'imperatif':
            endings = ['e', 'ons', 'ez', ]
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + stem + 'e'
                elif nombre == 'pluriel':
                    return 'Nous ' + stem + 'ons'
            elif personne == '2':
                if nombre=='singulier':
                    return 'NON'
                elif nombre == 'pluriel':
                    return 'Vous ' + stem + 'ez'
            if personne == '3':
                if nombre == 'singulier':
                    return "NON"
                elif nombre == 'pluriel':
                    return "NON"
        elif mode == 'conditionel':
            endings = ['erais', 'erais', 'erait', 'erions', 'eriez', 'eraient']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + verb + 'ais'
                elif nombre == 'pluriel':
                    return 'Nous ' + verb + 'ions'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + verb + 'ais'
                elif nombre == 'pluriel':
                    return 'Vous ' + verb + 'iez'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + verb + 'ait'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + verb + 'aient'
        elif mode == 'infinitif':
            return verb 
        elif mode == 'participe':
            return stem+ 'ant'
        else:
            return 'Mode non valide'
        
    elif temps == 'imparfait':
        if mode == 'indicatif':
            endings = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + stem + 'ais'
                elif nombre == 'pluriel':
                    return 'Nous ' + stem + 'ions'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + stem + 'ais'
                elif nombre == 'pluriel':
                    return 'Vous ' + stem + 'iez'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + stem + 'ait'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + stem + 'aient'
        elif mode == 'subjunctif':
            endings = ['asse', 'asses', 'ât', 'assions', 'assiez', 'assent']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + stem + 'asse'
                elif nombre == 'pluriel':
                    return 'Nous ' + stem + 'assions'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + stem + 'asses'
                elif nombre == 'pluriel':
                    return 'Vous ' + stem + 'assiez'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + stem + 'ât'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + stem + 'assent'
        elif mode == 'imperatif':
            return 'NON'           
        elif mode == 'conditionel':
            return 'NON'
        elif mode == 'infinitif':
            return verb
        else:
            return 'Mode non valide'
    elif temps == 'futur':
        if mode == 'indicatif':
            endings = ['erai', 'eras', 'era', 'erons', 'erez', 'eront']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + verb + 'ai'
                elif nombre == 'pluriel':
                    return 'Nous ' + verb + 'ons'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + verb + 'as'
                elif nombre == 'pluriel':
                    return 'Vous ' + verb + 'ez'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + verb + 'a'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + verb + 'ont'
        elif mode == 'subjunctif':
            return 'NON'
        elif mode == 'imperatif':
            return 'NON'
        elif mode == 'conditionel':
            return 'NON'
        elif mode == 'infinitif':
            return verb
        else:
            return 'Mode non valide'
    if temps == 'passé':
        if mode == 'indicatif':
            endings = ['ai', 'as', 'a', 'âmes', 'âtes', 'èrent']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + stem + 'ai'
                elif nombre == 'pluriel':
                    return 'Nous ' + stem + 'âmes'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + stem + 'as'
                elif nombre == 'pluriel':
                    return 'Vous ' + stem + 'âtes'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + stem + 'a'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + stem + 'èrent'
        elif mode == 'subjunctif':
            endings = ['é', 'é', 'é', 'é', 'é', 'é']
            if personne == '1':
                if nombre == 'singulier':
                    return 'Je ' + stem + 'é'
                elif nombre == 'pluriel':
                    return 'Nous ' + stem + 'é'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'Tu ' + stem + 'é'
                elif nombre == 'pluriel':
                    return 'Vous ' + stem + 'é'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'Il/Elle ' + stem + 'é'
                elif nombre == 'pluriel':
                    return 'Ils/Elles ' + stem + 'é'
        elif mode == 'imperatif':
            endings = ['erais', 'erais', 'erait', 'erions', 'eriez', 'eraient']
            if personne == '1':
                if nombre == 'singulier':
                    return "J'aie" + stem + 'é'
                elif nombre == 'pluriel':
                    return 'Nous ayons' + stem + 'é'
            elif personne == '2':
                if nombre == 'singulier':
                    return 'NON'
                if nombre == 'pluriel':
                    return 'Vous ayez' + stem+ 'é'
            elif personne == '3':
                if nombre == 'singulier':
                    return 'NON'
                if nombre == 'pluriel':
                    return 'NON'
        elif mode == 'conditionel':
            return 'NON'
        elif mode == 'infinitif':
            return verb
        elif mode == 'participe':
            return stem + 'é'
        else:
            return 'Mode non valide'
    else:
        return 'Temps non valide'
    
print('Bienvenue dans le conjugueur de verbes !')
verbe = conjugaison()
print('Le verbe conjugué est :', verbe)
