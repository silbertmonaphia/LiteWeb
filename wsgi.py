from blog import application

if __name__ == '__main__':
    application.debug = True
    #context = ('/etc/ssl/certs/1_smona.info_bundle.crt', '/etc/ssl/private/2_smona.info.key')
    application.run(host='0.0.0.0', port=5001)
