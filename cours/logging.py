import logging

logging.basicConfig(level=logging.CRITICAL,
					filename="app.log",
					filemode='w')

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")