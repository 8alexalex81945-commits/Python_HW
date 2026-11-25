from smartphone import Smartphone

catalog = [Smartphone("<Samsung>",  "<Galaxy S26>.", "<+79999999999> ."),
           Smartphone("<Realmi>", "<16 Pro +>.", "<+79995555555> ."),
           Smartphone("<Xiaomi>", "<Redmi Note 15 Pro+>.", "<+79995555577> ."),
           Smartphone("<Apple>", "<iPhone 18 Pro Max>.", "<+79995555588> ."),
           Smartphone("<Google>", "<Pixel 11 Pro>.", "<+79995555599> .")]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model} "
          f" -  {smartphone.subscriber_number}")
