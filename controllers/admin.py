def approveusers():
    users = db(db.auth_user.registration_key == 'pending').select(db.auth_user.id,
                                                                  db.auth_user.first_name, db.auth_user.last_name,
                                                                  db.auth_user.email,
                                                                  db.auth_user.registration_key)

    return dict(users=users)

# Think
def unapproveusers():
    users = db(db.auth_user.registration_key != 'pending').select(db.auth_user.id,
                                                                  db.auth_user.first_name, db.auth_user.last_name,
                                                                  db.auth_user.email,
                                                                  db.auth_user.registration_key)
    return dict(users=users)


def ajaxapprove():
    # This allows managers to approve pending registrations
    userid = request.args[0]
    upd = ''
    responsetext = 'User ' + str(userid) + ' has been approved'
    messagetxt = 'Your registration request has been approved'
    link = URL('default', 'index', scheme=True, host=True)
    footnote = 'You can now access the site at: ' + link
    if len(request.args) > 1:
        upd = 'pending'
        responsetext = 'User ' + str(userid) + ' has been left at pending for now'

    db(db.auth_user.id == userid).update(registration_key=upd)


    return responsetext
