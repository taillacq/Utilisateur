# encoding: UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class Actionwords:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver_wait = WebDriverWait(self._driver,10)

        self._url = "https://internal-api-m2a.dev-open-payment.fr/auth/admin/master/console/"
        # self.values_role_CloudFareWeb = {"ABT", "AccessControl", "AccessControlFullAccess", "AlertConfiguration", "AlertManagement", "AlertReport", "CommsMonitor", "DeleteService", "DeviceDatasetDeployment", "EstateManagement", "EventGroupConfiguration",
        #             "FareRules", "LegacyStages", "operator", "ProductEditor", "Quarantine", "Report", "RouteManagement", "ScheduleManager", "ScheduleManagerImportScheduleData", "StaffReport", "SystemConfiguration", "TicketEditor",
        #             "Topology", "TvmReport", "validator.reader"}

    def g_open_session(self, url, wrt_element_type = "", wrt_negation = "", user_type = "", free_text = ""):
        # TODO: Implement action: "Une session %s %s a %s été ouverte" % (wrt_element_type, device_type, wrt_negation)
        self._driver.get(self._url)
        self._driver_wait.until(EC.visibility_of_element_located((By.ID,"username")))
        self._driver.find_element_by_id("username").clear()
        self._driver.find_element_by_id("password").clear()
        self._driver.find_element_by_id("username").send_keys("etaillacq")
        self._driver.find_element_by_id("password").send_keys("Fr4nc1sc0")
        self._driver.find_element_by_id("kc-login").send_keys(Keys.RETURN)

    def w_open_module(self, element_value):
        # TODO: Implement action: "Ouvrir le module *%s*" % (element_value)
        self._driver_wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[1]/table/tbody/tr[3]/td/a")))
        self._driver.find_element_by_link_text("m2a").click()

    def w_add_element(self, element_type, element_value):
        # TODO: Implement action: "Ajouter %s %s" % (element_type, element_value)
        self._driver_wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Users")))
        self._driver.find_element_by_link_text("Users").click()
        self._driver_wait.until(EC.visibility_of_element_located((By.ID, "createUser")))
        self._driver.find_element_by_id("createUser").click()
        self._driver_wait.until(EC.visibility_of_element_located((By.ID, "username")))
        self._driver.find_element_by_id("username").send_keys(element_value)
        self._driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()


    def w_insert_element(self, element_type, wrt_additional_informations):
        # TODO: Implement action: "Insérer %s %s" % (element_type, wrt_additional_informations)
        self._driver_wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Credentials")))
        self._driver.find_element_by_link_text("Credentials").click()
        self._driver_wait.until(EC.visibility_of_element_located((By.ID, "newPas")))
        self._driver.find_element_by_id("newPas").send_keys(wrt_additional_informations)
        self._driver.find_element_by_id("confirmPas").send_keys(wrt_additional_informations)
        self._driver.find_element_by_xpath("//button[contains(.,'Set Password')]").click()
        self._driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-danger")))
        #self._driver.switch_to.alert.accept()
        self._driver.find_element_by_css_selector(".btn-danger").click()


    def w_assign_element(self, element_type, element_value, element_status = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Attribuer %s %s à %s %s" % (element_type, element_value, element_status, wrt_additional_informations)
        self._driver.refresh()
        self._driver_wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Role Mappings")))
        self._driver.find_element_by_link_text("Role Mappings").click()
        self._driver_wait.until(EC.visibility_of_element_located((By.ID, "s2id_clients")))
        self._driver.find_element_by_id("s2id_clients").click()
        self._driver.find_element_by_class_name("select2-input").click()
        self._driver.find_element_by_class_name("select2-input").send_keys(element_value)
        self._driver.find_element_by_class_name("select2-input").click()
        self._driver.find_element_by_class_name("select2-input").send_keys(Keys.RETURN)


        self._driver_wait.until(EC.visibility_of_element_located((By.ID, "available-client")))
        select = Select(self._driver.find_element_by_id("available-client"))

        for value in select.options:
            select.select_by_visible_text(value.text)

        self._driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()


    def t_create_element(self, element_type, element_value, wrt_additional_informations, wrt_negation = ""):
        # TODO: Implement result: "%s est %s créé(e) %s et visible %s" % (element_type, wrt_negation, element_value, wrt_additional_informations)
        self._driver.find_element_by_link_text("Users").click()
        assert element_value in self._driver.page_source




    def g_open_browser(self, element_label = "", url = ""):
        # TODO: Implement action: "%s est ouvert à l'adresse : %s" % (element_label, url)
        raise NotImplementedError

    def t_open_session(self, element_value = "", wrt_additional_informations = ""):
        # TODO: Implement result: "La demande de connexion est %s" % (element_value)
        # TODO: Implement result: "%s" % (wrt_additional_informations)
        raise NotImplementedError

    def g_start_application(self, application_type = "", wrt_additionnal_information = ", l'application se trouve sur l'écran de connexion"):
        # TODO: Implement action: "%s est démarrée%s" % (application_type, wrt_additionnal_information)
        raise NotImplementedError

    def g_have_right(self, element_label = "", element_value = "", wrt_negation = ""):
        # TODO: Implement action: "L'agent possède %s le droit : %s pour %s" % (wrt_negation, element_label, element_value)
        raise NotImplementedError

    def w_access_menu(self, element_label = ""):
        # TODO: Implement action: "Accéder au menu : %s" % (element_label)
        raise NotImplementedError

    def t_access_right(self, element_type = "", element_label = ""):
        # TODO: Implement result: "%s est accessible avec le droit %s" % (element_type, element_label)
        raise NotImplementedError

    def w_edit_agent(self, element_type = ""):
        # TODO: Implement action: "Sélectionner un des agents %s dans la liste" % (element_type)
        # TODO: Implement action: "Ouvrir la fiche de l'agent"
        # TODO: Implement action: "Passer en mode édition"
        raise NotImplementedError

    def w_open_tab(self, element_value = ""):
        # TODO: Implement action: "Accéder à l'onglet *%s*" % (element_value)
        raise NotImplementedError

    def t_assign_element(self, element_type = "", element_value = ""):
        # TODO: Implement result: "%s est affectable %s" % (element_type, element_value)
        raise NotImplementedError

    def t_change_issue(self, wrt_behavior_result = "sont sauvegardées"):
        # TODO: Implement result: "Les modifications %s" % (wrt_behavior_result)
        raise NotImplementedError

    def w_search_customer(self, element_type = ""):
        # TODO: Implement action: "Rechercher un client %s" % (element_type)
        # TODO: Implement action: "Saisir le nom du client"
        # TODO: Implement action: "Saisir le prénom du client"
        # TODO: Implement action: "Valider les informations de recherche"
        raise NotImplementedError

    def t_search_customer(self, element_status = "", wrt_behavior_result = "", wrt_additional_informations = ""):
        # TODO: Implement result: "Le client est %s" % (element_status)
        # TODO: Implement result: "%s" % (wrt_behavior_result)
        # TODO: Implement result: "%s" % (wrt_additional_informations)
        raise NotImplementedError

    def w_access_element(self, element_value = "", element_type = "", free_text = ""):
        # TODO: Implement action: "Accéder à %s %s" % (element_type, element_value)
        raise NotImplementedError

    def t_access_element(self, element_value = "", element_type = ""):
        # TODO: Implement result: "%s %s est accessible" % (element_type, element_value)
        raise NotImplementedError

    def t_delete_element(self, element_type = "", wrt_additional_informations = ""):
        # TODO: Implement result: "%s est supprimé(e) %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def t_display_screen(self, element_label = "", mode = ""):
        # TODO: Implement result: "L'écran %s s'affiche %s" % (element_label, mode)
        raise NotImplementedError

    def g_open_module(self, element_value = ""):
        # TODO: Implement action: "Le module %s a été ouvert" % (element_value)
        raise NotImplementedError

    def g_display_element(self, wrt_element_type = "", element_type = "", element_label = "", wrt_additional_informations = "", free_text = "", datatable = "||"):
        # TODO: Implement action: "%s %s est affiché(e) %s" % (wrt_element_type, element_label, wrt_additional_informations)
        raise NotImplementedError

    def w_create_version(self, element_type = ""):
        # TODO: Implement action: "Créer une nouvelle version de %s" % (element_type)
        raise NotImplementedError

    def w_edit_version_status(self, element_status = "", element_type = ""):
        # TODO: Implement action: "Editer la version %s" % (element_type)
        # TODO: Implement action: "Passer le statut à *%s*" % (element_status)
        raise NotImplementedError

    def w_export_version(self, element_type = ""):
        # TODO: Implement action: "Sélectionner la version de %s à exporter" % (element_type)
        # TODO: Implement action: "Cliquer sur Exporter"
        raise NotImplementedError

    def w_add_product_basket(self, element_type = ""):
        # TODO: Implement action: "Ajouter le produit %s au panier" % (element_type)
        raise NotImplementedError

    def w_distribute_basket(self):
        # TODO: Implement action: "Distribuer le contenu du panier"
        raise NotImplementedError

    def g_add_element(self, element_type = "", element_label = "", wrt_additional_informations = ""):
        # TODO: Implement action: "%s %s a été ajouté(e) %s" % (element_type, element_label, wrt_additional_informations)
        raise NotImplementedError

    def t_print_element(self, wrt_negation = "", element_type = "", wrt_additional_informations = ""):
        # TODO: Implement result: "%s est %s imprimé(e) %s" % (element_type, wrt_negation, wrt_additional_informations)
        raise NotImplementedError

    def w_regularize_element(self, wrt_additional_informations = "", element_type = ""):
        # TODO: Implement action: "Régulariser %s %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def t_regularize_element(self, wrt_additional_informations = "", element_type = ""):
        # TODO: Implement result: "%s est régularisé(e) %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def w_input_element(self, element_type = "", element_value = "", element_name = ""):
        # TODO: Implement action: "Saisir %s %s" % (element_type, element_value)
        raise NotImplementedError

    def t_display_product(self, element_label = "", wrt_negation = ""):
        # TODO: Implement result: "Le %s est %s proposé à la vente" % (element_label, wrt_negation)
        raise NotImplementedError

    def w_finalize_sale(self, wrt_negation = ""):
        # TODO: Implement action: "Finaliser %s la vente" % (wrt_negation)
        raise NotImplementedError

    def g_made_sale(self, element_value = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Une vente %s a été effectuée %s" % (element_value, wrt_additional_informations)
        raise NotImplementedError

    def t_display_data(self, element_type = ""):
        # TODO: Implement result: "Le rapport affiche : %s" % (element_type)
        raise NotImplementedError

    def g_validate_product(self, wrt_additional_informations = "", wrt_behavior_result = "", free_text = ""):
        # TODO: Implement action: "Une validation %s a été effectuée %s" % (wrt_additional_informations, wrt_behavior_result)
        raise NotImplementedError

    def w_delete_element(self, element_type = ""):
        # TODO: Implement action: "Supprimer %s" % (element_type)
        raise NotImplementedError

    def t_accept_element(self, element_value = "", element_type = ""):
        # TODO: Implement result: "%s %s est accepté(e)" % (element_type, element_value)
        raise NotImplementedError

    def w_close_session(self, device_type = ""):
        # TODO: Implement action: "Fermer la session %s" % (device_type)
        raise NotImplementedError

    def w_copy_file(self, element_value = "", file_type = ""):
        # TODO: Implement action: "Le fichier %s est copié dans le dossier *%s*" % (file_type, element_value)
        raise NotImplementedError

    def w_process_flow_exchange_server(self, element_type = "", element_value = ""):
        # TODO: Implement action: "Le fichier est traité par le processus %s" % (element_type)
        # TODO: Implement action: "Ouvrir le groupe de process %s" % (element_value)
        # TODO: Implement action: "Entrer dans différents processors pour suivre l'état du flux"
        # TODO: Implement action: "1 - Clique droit sur un processors, sélectionner \"Data Provenance\"
        # 2 - Sur la première ligne clicker sur \"ShowLineage\"
        # 3 - Click droit sur le gros nœud rouge et sélectionner \"Show détails\"
        # 4 - Télécharger le flux via l'onglet \"Content\""
        # TODO: Implement result: "Le flux transite : le fichier généré est déposé dans le dossier de sortie"
        raise NotImplementedError

    def w_use_yatt(self, card_type = "", electronic_serial_number = ""):
        # TODO: Implement action: "Ouvrir l'application YATT, et présenter le support  %s %s sur la cible" % (cardType, electronicSerialNumber)
        raise NotImplementedError

    def t_distribute_product(self, wrt_behavior_result = "", wrt_additional_informations = "", hosted_product = ""):
        # TODO: Implement result: "%s est distribué(e) %s" % (hostedProduct, wrt_additional_informations)
        # TODO: Implement result: "%s" % (wrt_behavior_result)
        raise NotImplementedError

    def g_encode_media(self, card_type = "", wrt_additional_informations = "", hosted_product = ""):
        # TODO: Implement action: "Le support %s %s" % (cardType, wrt_additional_informations)
        raise NotImplementedError

    def w_select_service(self, element_type = "", element_label = ""):
        # TODO: Implement action: "Sélectionner le service %s : *%s*" % (element_label, element_type)
        raise NotImplementedError

    def t_process_request(self, wrt_additional_informations = "", element_type = "", wrt_negation = ""):
        # TODO: Implement result: "La demande %s est %s prise en compte" % (element_type, wrt_negation)
        # TODO: Implement result: "%s" % (wrt_additional_informations)
        raise NotImplementedError

    def g_install_soft(self, application_type = ""):
        # TODO: Implement action: "Le logiciel %s à été installé" % (application_type)
        raise NotImplementedError

    def t_verify_element_value(self, element_label = "", element_value = "", free_text = ""):
        # TODO: Implement result: "La valeur pour %s est %s" % (element_label, element_value)
        raise NotImplementedError

    def w_buy_product(self, element_type = ""):
        # TODO: Implement action: "Acheter un produit %s" % (element_type)
        raise NotImplementedError

    def w_deposit_media(self, device_type = "", card_type = "", electronic_serial_number = ""):
        # TODO: Implement action: "Présenter le support %s %s sur la cible %s" % (cardType, electronicSerialNumber, device_type)
        raise NotImplementedError

    def t_acknowledgement_element(self, element_type = ""):
        # TODO: Implement result: "Un acquittement %s est généré" % (element_type)
        raise NotImplementedError

    def w_open_file(self, file_type = "", element_label = "", element_value = ""):
        # TODO: Implement action: "Ouvrir le fichier %s %s %s" % (file_type, element_label, element_value)
        raise NotImplementedError

    def g_generate_file(self, file_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Un fichier %s a été généré %s" % (file_type, wrt_additional_informations)
        raise NotImplementedError

    def w_upload_file(self, file_type = "", intput_folder = "", output_folder = ""):
        # TODO: Implement action: "Déposer le fichier %s %s %s" % (file_type, intput_folder, output_folder)
        raise NotImplementedError


    def t_create_version(self, element_value = "", element_type = "", wrt_negation = ""):
        # TODO: Implement result: "La version %s de %s est %s créée" % (element_value, element_type, wrt_negation)
        raise NotImplementedError

    def t_make_inspection(self, wrt_behavior_result = ""):
        # TODO: Implement result: "Le contrôle est %s" % (wrt_behavior_result)
        raise NotImplementedError

    def t_finalize_import(self, wrt_behavior_result = ""):
        # TODO: Implement result: "L'importation est terminée avec %s" % (wrt_behavior_result)
        raise NotImplementedError

    def t_generate_activity(self, device_type = "", element_type = ""):
        # TODO: Implement result: "Le %s génère une activité %s" % (device_type, element_type)
        raise NotImplementedError

    def t_contents_element(self, element_value = "", element_type = "", datatable = "||", free_text = ""):
        # TODO: Implement result: "%s contient %s" % (element_type, element_value)
        raise NotImplementedError

    def w_select_element(self, wrt_element_type = "", element_value = "", element_type = "", wrt_negaction = ""):
        # TODO: Implement action: "%sSélectionner %s %s" % (wrt_negaction, wrt_element_type, element_value)
        raise NotImplementedError

    def w_execute_script(self, element_label = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Executer le script : %s %s" % (element_label, wrt_additional_informations)
        raise NotImplementedError

    def g_update_server(self, device_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Le fichier d'installation %s est copié sur serveur %s" % (device_type, wrt_additional_informations)
        raise NotImplementedError

    def t_finalize_installation(self):
        # TODO: Implement result: "L'installation de l'équipement est terminée avec succès"
        # TODO: Implement result: "L'équipement se met en service"
        raise NotImplementedError

    def g_update_device(self):
        # TODO: Implement action: "La version logiciel à été importée depuis transfolio et exportée dans le référenciel"
        raise NotImplementedError

    def w_synchronize_device(self, device_type = ""):
        # TODO: Implement action: "Synchroniser %s avec le serveur" % (device_type)
        raise NotImplementedError

    def t_download_element(self, element_type = "", file_type = ""):
        # TODO: Implement result: "%s télécharge %s" % (element_type, file_type)
        raise NotImplementedError

    def t_reboot_device(self):
        # TODO: Implement result: "L'équipement reboot"
        raise NotImplementedError

    def t_update_element(self, element_type = "", element_value = ""):
        # TODO: Implement result: "%s est mis(e) à jour %s" % (element_type, element_value)
        raise NotImplementedError

    def s_check_list(self, action = ""):
        # TODO: Implement result: "%s" % (action)
        raise NotImplementedError

    def t_state_button(self, element_label = "", element_status = ""):
        # TODO: Implement result: "Le bouton *%s* est %s" % (element_label, element_status)
        raise NotImplementedError

    def g_generate_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "%s a été généré(e) %s" % (element_type, element_value)
        raise NotImplementedError

    def g_connect_element(self, connexion_type = "", element_type = "", wrt_negation = ""):
        # TODO: Implement action: "La connexion depuis %s est %s établie avec %s" % (element_type, wrt_negation, connexion_type)
        raise NotImplementedError

    def w_unzip_file(self, element_label = ""):
        # TODO: Implement action: "Décompresser le fichier %s" % (element_label)
        raise NotImplementedError

    def t_create_file(self, output_folder = "", element_type = "", wrt_negation = ""):
        # TODO: Implement result: "Le fichier %s est %s créé" % (element_type, wrt_negation)
        # TODO: Implement result: "Il est %s présent dans le dossier : %s" % (wrt_negation, output_folder)
        raise NotImplementedError

    def w_go_folder(self, element_label = ""):
        # TODO: Implement action: "Aller dans le dossier *%s*" % (element_label)
        raise NotImplementedError

    def t_state_field(self, element_type = "", element_value = "", mode = ""):
        # TODO: Implement result: "Le champ %s %s %s
        # " % (element_type, element_value, mode)
        raise NotImplementedError

    def g_define_element(self, element_type = "", element_label = "", element_value = "", device_type = ""):
        # TODO: Implement action: "%s %s est défini(e) avec la valeur %s pour %s
        # " % (element_type, element_label, element_value, device_type)
        raise NotImplementedError

    def w_update_element(self, element_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Mettre à jour %s %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def t_receive_sae_message(self, wrt_additional_informations = ""):
        # TODO: Implement result: "Un message SAE *%s* est reçu" % (wrt_additional_informations)
        raise NotImplementedError

    def g_generate_activity(self, wrt_additional_informations = "", element_type = ""):
        # TODO: Implement action: "Une activité %s a été générée %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def t_synchronize_element(self, element_type = "", action = "", wrt_negation = "", element_value = ""):
        # TODO: Implement result: "%s%s est %s synchronisé(e) avec %s " % (element_type, element_value, wrt_negation, action)
        raise NotImplementedError

    def t_process_sae_message(self, wrt_additional_informations = ""):
        # TODO: Implement result: "Le message SAE est traité : %s" % (wrt_additional_informations)
        raise NotImplementedError

    def w_input_billing_data(self):
        # TODO: Implement action: "Saisir les informations d'échéancier :"
        # TODO: Implement action: "- Paiement du 1er mois comptant"
        # TODO: Implement action: "- Le jour de prélèvement"
        # TODO: Implement action: "- La date de début du prélèvement"
        # TODO: Implement action: "- Le nombre d'échéances"
        # TODO: Implement action: "- La fréquence du prélèvement"
        # TODO: Implement action: "- Libellé (Nom du produit distribué)"
        raise NotImplementedError

    def w_input_banking_data(self):
        # TODO: Implement action: "Saisir les informations bancaires :"
        # TODO: Implement action: "- Client (pour sélectionner le compte d'un autre client \"payeur\" le cas échéant)"
        # TODO: Implement action: "- Libellé compte"
        # TODO: Implement action: "- BIC"
        # TODO: Implement action: "- IBAN"
        raise NotImplementedError

    def g_configure_element(self, element_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "%s a été configuré(e) %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def w_exceeded_element(self, element_type = ""):
        # TODO: Implement action: "Le délai %s est dépassé" % (element_type)
        raise NotImplementedError

    def w_set_group_element(self, element_value = "", element_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Sélectionner %s" % (element_value)
        # TODO: Implement action: "%s est %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def w_open_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "Ouvrir %s %s" % (element_type, element_value)
        raise NotImplementedError

    def t_contents_activity(self, wrt_behavior_result = "", wrt_element_type = ""):
        # TODO: Implement result: "Un fichier d'activité %s est généré" % (wrt_element_type)
        # TODO: Implement result: "L'activité contient %s" % (wrt_behavior_result)
        raise NotImplementedError

    def t_encode_media_field(self, media_application = "", media_section = "", element_label = "", element_value = ""):
        # TODO: Implement result: "Depuis la section %s %s, le champ %s possède %s" % (mediaApplication, mediaSection, element_label, element_value)
        raise NotImplementedError

    def t_display_message(self, element_label = "", free_text = ""):
        # TODO: Implement result: "Le message : %s s'affiche" % (element_label)
        raise NotImplementedError

    def t_state_media(self, element_status = ""):
        # TODO: Implement result: "Le support %s" % (element_status)
        raise NotImplementedError

    def t_display_element(self, wrt_element_type = "", wrt_additional_informations = "", element_label = "", element_type = "", datatable = "||"):
        # TODO: Implement result: "%s %s s'affiche %s" % (wrt_element_type, element_label, wrt_additional_informations)
        raise NotImplementedError

    def t_open_element(self, element_type = "", wrt_additional_informations = ""):
        # TODO: Implement result: "%s s'ouvre %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError


    def w_execute_command(self, element_value = "", element_type = "", element_label = ""):
        # TODO: Implement action: "Exécuter la commande %s %s %s" % (element_type, element_label, element_value)
        raise NotImplementedError

    def t_process_element(self, element_type = "", element_status = ""):
        # TODO: Implement result: "%s est effectué(e) %s" % (element_status, element_type)
        raise NotImplementedError

    def s_crud_test(self, action = "", wrt_additional_informations = ""):
        # TODO: Implement action: "%s" % (action)
        # TODO: Implement result: "%s" % (wrt_additional_informations)
        raise NotImplementedError

    def w_create_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "Créer %s %s" % (element_type, element_value)
        raise NotImplementedError

    def w_generate_colored_list(self, element_type = ""):
        # TODO: Implement action: "Générer une liste %s" % (element_type)
        raise NotImplementedError

    def t_edit_element(self, element_type = "", element_value = "", element_localization = ""):
        # TODO: Implement result: "%s est modifié(e) %s et visible %s" % (element_type, element_value, element_localization)
        raise NotImplementedError


    def t_accordance_element(self, element_type = "", element_value = ""):
        # TODO: Implement result: "L'information sur %s correspond à la valeur attendue %s" % (element_type, element_value)
        raise NotImplementedError

    def w_display_element(self, element_type = ""):
        # TODO: Implement action: "Afficher %s" % (element_type)
        raise NotImplementedError

    def t_import_details(self, wrt_behavior_result = "", wrt_additional_informations = ""):
        # TODO: Implement result: "Le résultat de l'import est affiché, l'import %s" % (wrt_behavior_result)
        # TODO: Implement result: "%s" % (wrt_additional_informations)
        raise NotImplementedError

    def w_print_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "Imprimer %s %s" % (element_type, element_value)
        raise NotImplementedError

    def t_process_file(self, element_type = "", element_status = "", wrt_additional_informations = ""):
        # TODO: Implement result: "Le fichier %s est traité %s" % (element_type, element_status)
        # TODO: Implement result: "Le fichier est déposé dans %s" % (wrt_additional_informations)
        raise NotImplementedError

    def w_collect_device_information(self, device_type = "", connexion_type = "", file_type = ""):
        # TODO: Implement action: "La connexion avec %s est établie avec %s" % (device_type, connexion_type)
        # TODO: Implement action: "Télécharger l'information %s" % (file_type)
        raise NotImplementedError

    def g_synchronize_element(self, wrt_element_type = "", wrt_element_value = "", wrt_element_status = "", wrt_negation = "", element_type = ""):
        # TODO: Implement action: "%s %s a été %s synchronisé(e) %s" % (wrt_element_type, wrt_element_value, wrt_negation, wrt_element_status)
        raise NotImplementedError

    def g_process_element(self, element_type = "", element_value = "", action = ""):
        # TODO: Implement action: "%s a été %s %s" % (element_type, action, element_value)
        raise NotImplementedError

    def w_execute_jvisualvm_job(self, element_label = "", element_value = ""):
        # TODO: Implement action: "Ouvrir JVisualVM"
        # TODO: Implement action: "Exécuter le job : *%s* avec le paramètre : *%s*" % (element_label, element_value)
        raise NotImplementedError

    def g_execute_element(self, element_type = "", element_value = "", wrt_additional_informations = ""):
        # TODO: Implement action: "%s %s à été éxécuté(e) %s" % (element_type, element_value, wrt_additional_informations)
        raise NotImplementedError

    def w_open_bi_report(self, element_type = ""):
        # TODO: Implement action: "Ouvrir un rapport %s Infocentre " % (element_type)
        raise NotImplementedError

    def g_state_element(self, element_type = "", wrt_additional_informations = "", element_status = ""):
        # TODO: Implement action: "%s est %s %s" % (element_type, element_status, wrt_additional_informations)
        raise NotImplementedError

    def s_setting_wheel(self, pause_rotation = "", rotation_speed = "", electronic_serial_number = ""):
        # TODO: Implement action: "L'automate de validation est nécessaire pour le test"
        # TODO: Implement action: "L'automate à une configuration de *%s* de temps de pause et *%s* de vitesse de rotation" % (pause_rotation, rotation_speed)
        # TODO: Implement action: "Les %s supports sont placés sur l'automate" % (electronicSerialNumber)
        raise NotImplementedError

    def s_validate_wheel(self, electronic_serial_number = "", wrt_behavior_result = "", device_type = "", acceptance_rate = ""):
        # TODO: Implement result: "Le %s détecte le support présenté à chaque passage" % (device_type)
        # TODO: Implement result: "%s" % (wrt_behavior_result)
        # TODO: Implement result: "Le %s traite %s" % (device_type, electronicSerialNumber)
        # TODO: Implement result: "Le taux d'acceptation  doit être de %s" % (acceptance_rate)
        raise NotImplementedError

    def g_integrate_data_plural(self, element_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Des données %s ont été intégrées %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def w_leave_element(self, device_type = "", element_type = ""):
        # TODO: Implement action: "Sortir du menu ou de la fonction en cours %s sur l'équipement %s" % (element_type, device_type)
        raise NotImplementedError

    def w_state_capping_thresold(self, device_type = "", element_status = ""):
        # TODO: Implement action: "Le seuil de replafonnement %s est %s" % (device_type, element_status)
        raise NotImplementedError

    def t_validate_first_travel(self, wrt_negation = "", wrt_behavior_result = ""):
        # TODO: Implement result: "Le produit est %s validé en première montée, un nouveau voyage %s" % (wrt_negation, wrt_behavior_result)
        raise NotImplementedError

    def w_waiting_time_limit(self, wrt_additional_informations = ""):
        # TODO: Implement action: "Attendre %s" % (wrt_additional_informations)
        raise NotImplementedError

    def g_localize_element(self, element_type = "", element_value = "", wrt_additional_informations = ""):
        # TODO: Implement action: "%s est %s %s" % (element_type, element_value, wrt_additional_informations)
        raise NotImplementedError

    def g_state_device(self, device_type = "", element_status = "", free_text = "", datatable = "||"):
        # TODO: Implement action: "%s a/est %s" % (device_type, element_status)
        raise NotImplementedError

    def w_open_session(self, device_type = "", wrt_additional_informations = "", login_value = "", pass_value = "", element_type = "Saisir l'identifiant"):
        # TODO: Implement action: "Ouvrir une session %s %s" % (device_type, wrt_additional_informations)
        # TODO: Implement action: "%s %s" % (element_type, login_value)
        # TODO: Implement action: "Saisir le mot de passe %s" % (pass_value)
        raise NotImplementedError

    def w_connect_customer_account(self):
        # TODO: Implement action: "Se connecter avec un compte client"
        raise NotImplementedError

    def t_allow_element(self, element_value = "", wrt_negation = ""):
        # TODO: Implement result: "Il est %s possible de %s" % (wrt_negation, element_value)
        raise NotImplementedError

    def w_action_manual(self, action = ""):
        # TODO: Implement action: "Manuellement : %s" % (action)
        raise NotImplementedError

    def t_state_device(self, device_type = "", element_status = "", action = "passe"):
        # TODO: Implement result: "%s %s à l'état %s" % (device_type, action, element_status)
        raise NotImplementedError

    def w_click_on_element(self, element_label = "", wrt_element_type = ""):
        # TODO: Implement action: "Cliquer sur %s %s" % (wrt_element_type, element_label)
        raise NotImplementedError

    def g_apply_colored_list(self, element_value = "", device_type = ""):
        # TODO: Implement action: "La dernière version de liste %s est appliquée par le %s" % (element_value, device_type)
        raise NotImplementedError

    def w_validate_media(self, element_status = "", device_type = "", card_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Présenter le support %s %s sur la cible %s %s" % (cardType, element_status, device_type, wrt_additional_informations)
        raise NotImplementedError

    def t_validate_media(self, device_type = "", wrt_behavior_result = "", element_status = "", wrt_additional_informations = ""):
        # TODO: Implement result: "%s affiche l'écran de validation %s" % (device_type, wrt_behavior_result)
        # TODO: Implement result: "L'icône de validation est %s" % (element_status)
        # TODO: Implement result: "Information de validation : %s est affiché(e)" % (wrt_additional_informations)
        raise NotImplementedError

    def g_use_rss_demo(self, application_type = "", element_type = ""):
        # TODO: Implement action: "Depuis le serveur démo SVD, sélectionner l'application %s et le type de lecteur %s" % (application_type, element_type)
        raise NotImplementedError

    def t_state_element(self, element_type = "", element_status = "", wrt_additional_informations = ""):
        # TODO: Implement result: "%s est %s %s" % (element_type, wrt_additional_informations, element_status)
        raise NotImplementedError

    def w_startup_device(self, device_type = ""):
        # TODO: Implement action: "Mettre sous tension le %s" % (device_type)
        raise NotImplementedError

    def s_state_transfolio(self, status_transfolio = "", status_esb = "", status_portal = "", domain_number = "", status_domain = ""):
        # TODO: Implement action: "Le domaine %s est %s
        # " % (domain_number, status_domain)
        # TODO: Implement action: "Transfolio est en %s" % (status_transfolio)
        # TODO: Implement action: "L'ESB est en %s" % (status_esb)
        # TODO: Implement action: "Le portail est en %s" % (status_portal)
        raise NotImplementedError

    def t_sale_element(self, element_type = "", wrt_additional_informations = "", device_type = ""):
        # TODO: Implement result: "%s %s est distribué(e) par le %s
        # " % (element_type, wrt_additional_informations, device_type)
        raise NotImplementedError

    def t_generate_element(self, element_value = "", wrt_additional_informations = "", element_type = ""):
        # TODO: Implement result: "%s %s est généré(e) %s" % (element_type, element_value, wrt_additional_informations)
        raise NotImplementedError

    def w_move_file(self, element_localization = "", element_type = ""):
        # TODO: Implement action: "Déplacer %s vers %s" % (element_type, element_localization)
        raise NotImplementedError

    def t_export_version(self, element_value = "", element_type = "", negation = ""):
        # TODO: Implement result: "La version %s %s est %s exportée" % (element_type, element_value, negation)
        raise NotImplementedError

    def w_edit_file_value(self, element_label = "", file_type = "", element_localization = "", element_type = "", element_value = ""):
        # TODO: Implement action: "Ouvrir le fichier %s %s dans le dossier : %s" % (file_type, element_label, element_localization)
        # TODO: Implement action: "Modifier la valeur de l'élément %s à %s" % (element_type, element_value)
        raise NotImplementedError

    def w_reboot_device(self):
        # TODO: Implement action: "Redémarrer l'équipement"
        raise NotImplementedError

    def g_change_element(self, element_type = "", action = ""):
        # TODO: Implement action: "%s a été %s " % (element_type, action)
        raise NotImplementedError

    def g_reload_element(self, element_type = ""):
        # TODO: Implement action: "Un rechargement %s a été effectué" % (element_type)
        raise NotImplementedError

    def w_import_file(self, element_type = "", device_type = ""):
        # TODO: Implement action: "Importer le fichier %s sur %s " % (element_type, device_type)
        raise NotImplementedError

    def g_import_element(self, elemeny_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Un import %s a été effectué %s" % (elemeny_type, wrt_additional_informations)
        raise NotImplementedError

    def t_detect_element(self, element_type = "", device_type = ""):
        # TODO: Implement result: "%s est détecté(e) %s" % (element_type, device_type)
        raise NotImplementedError

    def g_action_manual(self, action = ""):
        # TODO: Implement action: "Manuellement %s" % (action)
        raise NotImplementedError

    def t_activate_element(self, element_type = "", element_value = ""):
        # TODO: Implement result: "%s %s est activé(e)" % (element_type, element_value)
        raise NotImplementedError

    def g_open_element(self, element_type = "", file_type = "", element_localisation = ""):
        # TODO: Implement action: "%s %s %s est ouvert(e)" % (element_type, file_type, element_localisation)
        raise NotImplementedError

    def t_finalize_sale(self, wrt_negation = "", wrt_behavior_result = ""):
        # TODO: Implement result: "La vente est %s finalisée %s" % (wrt_negation, wrt_behavior_result)
        raise NotImplementedError

    def w_edit_element(self, element_type = "", element_localization = "", element_value = ""):
        # TODO: Implement action: "Modifier %s %s %s" % (element_type, element_value, element_localization)
        raise NotImplementedError

    def w_launch_soft(self, element_type = ""):
        # TODO: Implement action: "Exécuter %s" % (element_type)
        raise NotImplementedError

    def w_complete_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "Renseigner %s %s" % (element_type, element_value)
        raise NotImplementedError

    def w_remove_element(self, element_type = ""):
        # TODO: Implement action: "Retirer %s" % (element_type)
        raise NotImplementedError

    def t_generate_colored_list(self, element_type = ""):
        # TODO: Implement result: "Une nouvelle liste %s est générée" % (element_type)
        # TODO: Implement result: "Le numéro de version de la liste colorée est incrémenté de 1"
        raise NotImplementedError

    def t_attrib_media(self, card_type = ""):
        # TODO: Implement result: "Le support %s est attribué" % (cardType)
        raise NotImplementedError

    def w_execute_etl(self, element_type = "ETL"):
        # TODO: Implement action: "Exécuter un %s pour mettre à jour la base de données Infocentre" % (element_type)
        raise NotImplementedError

    def t_execute_element(self, wrt_behavior_result = "", element_type = "", wrt_negation = ""):
        # TODO: Implement result: "%s est %s exécuté(e) %s" % (element_type, wrt_negation, wrt_behavior_result)
        raise NotImplementedError

    def w_inspect_element(self, card_type = "", device_type = ""):
        # TODO: Implement action: "Effectuer un contrôle %s %s" % (cardType, device_type)
        raise NotImplementedError

    def w_cause_error(self, element_status = "", element_type = ""):
        # TODO: Implement action: "Provoquer une erreur %s %s" % (element_status, element_type)
        raise NotImplementedError

    def g_make_control(self, element_value = "", element_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Un contrôle %s %s a été effectué %s" % (element_type, element_value, wrt_additional_informations)
        raise NotImplementedError

    def t_custom_media(self, card_type = "", element_value = "", wrt_additional_informations = ""):
        # TODO: Implement result: "Le support %s est personnalisé de façon %s" % (cardType, element_value)
        # TODO: Implement result: "Les informations de personnalisation sont affichées %s" % (wrt_additional_informations)
        raise NotImplementedError

    def t_reconstitute_media(self):
        # TODO: Implement result: "Le support est reconstitué avec succès"
        # TODO: Implement result: "Le support est affecté au même client que le précédent"
        # TODO: Implement result: "Les contrats & profils présents sur le support initial sont présents sur le nouveau support dans les mêmes conditions"
        raise NotImplementedError

    def w_device_state(self, device_type = "", element_status = ""):
        # TODO: Implement action: "%s a/est %s" % (device_type, element_status)
        raise NotImplementedError

    def g_create_element(self, element_type = "", element_value = "", wrt_additional_informations = ""):
        # TODO: Implement action: "%s %s a été créé(e) %s" % (element_type, element_value, wrt_additional_informations)
        raise NotImplementedError

    def w_sale_element(self, element_type = "", datatable = "||"):
        # TODO: Implement action: "Effectuer une vente %s" % (element_type)
        raise NotImplementedError

    def t_verify_data_integrity(self, wrt_element_type = "", wrt_element_value = "", element_type = "", element_value = ""):
        # TODO: Implement result: "Le champ %s contient %s" % (wrt_element_type, wrt_element_value)
        raise NotImplementedError

    def w_set_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "Paramétrer %s %s" % (element_type, element_value)
        raise NotImplementedError

    def t_finalize_element(self, element_type = "", wrt_negation = ""):
        # TODO: Implement result: "L'opération %s est %s finalisée. " % (element_type, wrt_negation)
        raise NotImplementedError

    def w_connect_device(self, connexion_type = "", device_type = ""):
        # TODO: Implement action: "Se connecter à %s avec %s" % (device_type, connexion_type)
        raise NotImplementedError

    def t_transfer_element(self, element_type = "", element_value = "", action = ""):
        # TODO: Implement result: "%s est transféré(e) %s vers %s" % (element_type, element_value, action)
        raise NotImplementedError

    def w_receive_message_sae(self, element_value = "", device_type = ""):
        # TODO: Implement action: "Le SAE envoie un message : *%s* %s" % (element_value, device_type)
        raise NotImplementedError

    def w_export_referential(self, device_type = "", element_type = "", element_label = " sur l'équipement :"):
        # TODO: Implement action: "Exporter un référentiel de type %s%s%s" % (element_type, element_label, device_type)
        raise NotImplementedError

    def g_export_element(self, element_type = "", element_value = "", wrt_additional_informations = ""):
        # TODO: Implement action: "%s %s a été exporté(e) %s" % (element_type, element_value, wrt_additional_informations)
        raise NotImplementedError

    def w_scan_element(self, element_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Scanner %s %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def w_search_element(self, element_type = "", wrt_additional_informations = ""):
        # TODO: Implement action: "Rechercher %s" % (element_type)
        # TODO: Implement action: "Saisir %s" % (wrt_additional_informations)
        # TODO: Implement action: "Valider les informations de recherche"
        raise NotImplementedError

    def w_synchronize_element(self, element_type = "", element_value = "", wrt_negation = "", device_type = ""):
        # TODO: Implement action: "%s%s est %s synchronisé(e) avec %s " % (element_type, element_value, wrt_negation, device_type)
        raise NotImplementedError

    def g_acknowledgement_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "%s %s a été acquitté(e)" % (element_type, element_value)
        raise NotImplementedError

    def t_close_session(self, device_type = "", wrt_element_type = "", wrt_negation = ""):
        # TODO: Implement result: "%s ferme %s la session %s" % (device_type, wrt_negation, wrt_element_type)
        raise NotImplementedError

    def w_open_submodule(self, element_value = ""):
        # TODO: Implement action: "Accéder à la partie %s" % (element_value)
        raise NotImplementedError

    def w_expand_element(self, element_label = "", wrt_element_label = ""):
        # TODO: Implement action: "Développer %s" % (wrt_element_label)
        raise NotImplementedError

    def w_move_over_element(self, element_label = ""):
        # TODO: Implement action: "Se positionner sur %s" % (element_label)
        raise NotImplementedError

    def w_select_element_from_section(self, section_label = "", element_label = "", element_value = ""):
        # TODO: Implement action: "Dans la section %s" % (section_label)
        # TODO: Implement action: "Définir %s %s" % (element_label, element_value)
        raise NotImplementedError

    def w_check_element(self, element_label = ""):
        # TODO: Implement action: "(Dé)cocher %s " % (element_label)
        raise NotImplementedError

    def t_display_on_table(self, column_name = "", row_index = "", cell = "", wrt_element_type = "", wrt_additional_informations = ""):
        # TODO: Implement result: "%s %s est affiché(e) %s" % (wrt_element_type, cell, wrt_additional_informations)
        raise NotImplementedError

    def s_display_information(self, wrt_additional_informations = "", datatable = "||"):
        # TODO: Implement action: "%s" % (wrt_additional_informations)
        raise NotImplementedError

    def w_select_view(self, element_type = ""):
        # TODO: Implement action: "Sélectionner la vue %s" % (element_type)
        raise NotImplementedError

    def w_select_from_row(self, element_label = "", element_value = "", wrt_element_label = ""):
        # TODO: Implement action: "Sélectionner  %s %s" % (wrt_element_label, element_value)
        raise NotImplementedError

    def w_present_media(self, card_type = "", hosted_product = "", hosted_product_date_end = "", wrt_additional_informations = "", hosted_product_time_end = ""):
        # TODO: Implement action: "Présenter le support %s possédant un contrat %s %s" % (cardType, hostedProduct, wrt_additional_informations)
        raise NotImplementedError

    def t_result_validation(self, element_type = "", element_label = "", element_status = "", wrt_element_status = "", validation_type = "", wrt_validation_type = "", failure_reason = "", front_led_state = "", wrt_front_led_state = "", wrt_front_led_state_position = "", target_led_state = "", wrt_target_led_state = ""):
        # TODO: Implement result: "Le contrat %s est %s en validation %s" % (element_type, wrt_element_status, wrt_validation_type)
        # TODO: Implement result: "Le message '%s' s'affiche" % (element_label)
        # TODO: Implement result: "La LED de la cible est %s" % (wrt_targetLedState)
        # TODO: Implement result: "La LED en haut %s est %s" % (wrt_frontLedState_position, wrt_frontLedState)
        raise NotImplementedError

    def g_request_api(self, wrt_element_type = "", wrt_integrate_data = "", endpoint = "", method = "", page_size = "", page_number = ""):
        # TODO: Implement action: "L'élément : %s contenant les données %s a été intégré" % (wrt_element_type, wrt_integrate_data)
        # TODO: Implement action: "La requête REST utilisée est : %s %s" % (method, endpoint)
        raise NotImplementedError

    def w_define_media(self, electronic_serial_number = "", card_type = ""):
        # TODO: Implement action: "Pour le support %s avec le numéro de série %s" % (cardType, electronicSerialNumber)
        raise NotImplementedError

    def t_transfer_file(self, file_type = "", element_label = "", wrt_additional_informations = ""):
        # TODO: Implement result: "Le fichier %s nommé %s est transféré %s" % (file_type, element_label, wrt_additional_informations)
        raise NotImplementedError

    def w_refund_element(self, wrt_additional_informations = "", element_type = "une vente"):
        # TODO: Implement action: "Rembourser %s  %s" % (element_type, wrt_additional_informations)
        raise NotImplementedError

    def w_add_all_element(self, element_type = "", element_value = ""):
        # TODO: Implement action: "Ajouter tous %s %s" % (element_type, element_value)
        raise NotImplementedError

    def g_contents_element(self, element_type = "", element_label = "", element_value = ""):
        # TODO: Implement action: "%s %s contient %s" % (element_type, element_label, element_value)
        raise NotImplementedError

    def t_display_element_plural(self, wrt_element_type = "", wrt_additional_informations = "", element_label = "", element_type = ""):
        # TODO: Implement result: "%s %s sont affiché(e)s %s" % (wrt_element_type, element_label, wrt_additional_informations)
        raise NotImplementedError

    def w_send_request(self, device_type = "", element_label = ""):
        # TODO: Implement action: "%s envoie %s" % (device_type, element_label)
        raise NotImplementedError

    def t_remove_product(self, hosted_product = "", wrt_additional_informations = "", wrt_behavior_result = ""):
        # TODO: Implement result: "%s est résilié %s" % (hosted_product, wrt_additional_informations)
        # TODO: Implement result: "%s" % (wrt_behavior_result)
        raise NotImplementedError

    def g_integrate_data(self, wrt_element_type = "", wrt_integrate_data = "", endpoint = "", method = "", page_size = "", page_number = ""):
        # TODO: Implement action: "Les données %s contenant les données %s ont été intégrées" % (wrt_element_type, wrt_integrate_data)
        raise NotImplementedError

    def w_integrate_data(self, wrt_element_type = "", wrt_integrate_data = "", endpoint = "", method = "", page_size = "", page_number = ""):
        # TODO: Implement action: "Les données %s contenant les données %s ont été intégrées" % (wrt_element_type, wrt_integrate_data)
        raise NotImplementedError

    def w_contents_element(self, element_type = "", element_label = "", element_value = "", datatable = "||"):
        # TODO: Implement action: "%s %s contient %s" % (element_type, element_label, element_value)
        raise NotImplementedError

    def s_free_action(self, free_action = "", free_text = ""):
        # TODO: Implement action: "%s" % (free_action)
        raise NotImplementedError

    def s_free_result(self, free_result = ""):
        # TODO: Implement result: "%s" % (free_result)
        raise NotImplementedError

    def g_state_device(self):
        pass

    def state(self):
        pass

    def t_val(self):
        pass
