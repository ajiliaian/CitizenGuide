import json
import os
from datetime import datetime

class CountryRightsApp:
    def __init__(self):
        self.data_file = "country_rights.json"
        self.load_data()
        
    def load_data(self):
        """Məlumatları yüklə və ya nümunə məlumat yarat"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.countries = json.load(f)
        else:
            self.create_sample_data()
            
    def create_sample_data(self):
        """Nümunə ölkə məlumatları"""
        self.countries = {
            "Azerbaijan": {
                "description": "Azərbaycan Respublikası",
                "rights": [
                    "Həyat hüququ (Konstitusiya, maddə 27)",
                    "Şəxsi hüquqların toxunulmazlığı (maddə 28)",
                    "Düşüncə və vicdan azadlığı (maddə 47)",
                    "Söz azadlığı (maddə 48)",
                    "Toplantı azadlığı (maddə 49)",
                    "Məlumat almaq hüququ (maddə 50)",
                    "Əmək hüququ və iş seçmək azadlığı (maddə 35)",
                    "Təhsil hüququ (maddə 42)",
                    "Səhiyyə qayğısı hüququ (maddə 41)",
                    "Mülkiyyət hüququ (maddə 29)"
                ],
                "duties": [
                    "Qanunlara riayət etmək",
                    "Vergi ödəmək",
                    "Ölkəni müdafiə etmək",
                    "Təbiəti qorumaq",
                    "Digər insanların hüquqlarına hörmət etmək",
                    "Dövlət simvollarına hörmət etmək"
                ],
                "sources": [
                    "Azərbaycan Respublikasının Konstitusiyası",
                    "Əmək Məcəlləsi",
                    "Vətəndaş Məcəlləsi",
                    "İnzibati Xətalar Məcəlləsi"
                ],
                "last_updated": "2024-01-15"
            },
            "Turkey": {
                "description": "Türkiyə Respublikası",
                "rights": [
                    "Həyat hüququ (Konstitusiya, maddə 17)",
                    "Şəxsi hürriyyət və təhlükəsizlik hüququ (maddə 19)",
                    "Düşüncə və din azadlığı (maddə 24-25)",
                    "Söz və ifadə azadlığı (maddə 26)",
                    "Təşkilatlanma azadlığı (maddə 33)",
                    "Əmək hüququ (maddə 49)",
                    "Təhsil hüququ (maddə 42)",
                    "Səhiyyə hüququ (maddə 56)",
                    "Sosial təminat hüququ (maddə 60)"
                ],
                "duties": [
                    "Vergi ödəmək",
                    "Seçki hüququ və vəzifəsi",
                    "Hərbi xidmət",
                    "Qanunlara riayət etmək",
                    "İctimai xidmət"
                ],
                "sources": ["Türkiyə Respublikası Konstitusiyası"],
                "last_updated": "2024-01-10"
            },
            "USA": {
                "description": "Amerika Birləşmiş Ştatları",
                "rights": [
                    "Söz azadlığı (Birinci Düzəliş)",
                    "Silah daşımaq hüququ (İkinci Düzəliş)",
                    "Ədalətli mühakimə hüququ (Beşinci Düzəliş)",
                    "Sürətli və ədalətli mühakimə (Altıncı Düzəliş)",
                    "Vicdan azadlığı (Birinci Düzəliş)",
                    "Şəxsi həyat hüququ (Dördüncü Düzəliş)",
                    "İnsanlıq ləyaqəti",
                    "Bərabər müdafiə"
                ],
                "duties": [
                    "Seçkilərdə iştirak",
                    "Məhkəməyə şahidlik",
                    "Vergi ödəmək",
                    "Federal qanunlara riayət",
                    "Yerli qanunlara riayət"
                ],
                "sources": ["ABŞ Konstitusiyası", "Federal Qanunlar", "Ştat Konstitusiyaları"],
                "last_updated": "2024-01-05"
            }
        }
        self.save_data()
    
    def save_data(self):
        """Məlumatları fayla yaz"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.countries, f, ensure_ascii=False, indent=2)
    
    def list_countries(self):
        """Mövcud ölkələri göstər"""
        print("\n" + "="*50)
        print("MÖVCUD ÖLKƏLƏRİN SİYAHISI:")
        print("="*50)
        for i, country in enumerate(self.countries.keys(), 1):
            print(f"{i}. {country} - {self.countries[country]['description']}")
        print("="*50)
    
    def show_country_info(self, country_name):
        """Seçilmiş ölkənin məlumatlarını göstər"""
        if country_name in self.countries:
            country = self.countries[country_name]
            
            print("\n" + "═"*60)
            print(f"ÖLKƏ: {country_name}")
            print(f"Təsvir: {country['description']}")
            print(f"Son yenilənmə: {country['last_updated']}")
            print("═"*60)
            
            print("\n📜 HÜQUQLAR:")
            print("-"*40)
            for i, right in enumerate(country['rights'], 1):
                print(f"{i}. {right}")
            
            print("\n⚖️ VƏZİFƏLƏR:")
            print("-"*40)
            for i, duty in enumerate(country['duties'], 1):
                print(f"{i}. {duty}")
            
            print("\n📚 MƏNBƏLƏR:")
            print("-"*40)
            for source in country['sources']:
                print(f"• {source}")
            print("═"*60)
            
            self.show_comparison(country_name)
        else:
            print(f"\n⚠️ '{country_name}' adlı ölkə məlumat bazasında tapılmadı.")
    
    def show_comparison(self, selected_country):
        """Digər ölkələrlə müqayisə göstər"""
        print("\n🔍 MÜQAYISƏ (Digər ölkələrlə):")
        print("-"*50)
        
        selected_rights = set(self.countries[selected_country]['rights'])
        
        for country in self.countries:
            if country != selected_country:
                other_rights = set(self.countries[country]['rights'])
                common_rights = selected_rights.intersection(other_rights)
                
                if common_rights:
                    print(f"\n{selected_country} və {country} arasında ortaq hüquqlar:")
                    for right in list(common_rights)[:3]:  # İlk 3-ü göstər
                        print(f"  ✓ {right}")
                    if len(common_rights) > 3:
                        print(f"  ... və daha {len(common_rights)-3} ortaq hüquq")
    
    def add_country(self):
        """Yeni ölkə əlavə et"""
        print("\n➕ YENİ ÖLKƏ ƏLAVƏ ET")
        print("-"*40)
        
        name = input("Ölkənin adı: ").strip()
        if name in self.countries:
            print("⚠️ Bu ölkə artıq mövcuddur!")
            return
        
        description = input("Qısa təsvir: ").strip()
        
        print("\nHüquqları daxil edin (hər sətrə bir, boş sətir bitirmək üçün):")
        rights = []
        while True:
            right = input(f"Hüquq {len(rights)+1}: ").strip()
            if not right:
                break
            rights.append(right)
        
        print("\nVəzifələri daxil edin:")
        duties = []
        while True:
            duty = input(f"Vəzifə {len(duties)+1}: ").strip()
            if not duty:
                break
            duties.append(duty)
        
        print("\nMənbələri daxil edin:")
        sources = []
        while True:
            source = input(f"Mənbə {len(sources)+1}: ").strip()
            if not source:
                break
            sources.append(source)
        
        self.countries[name] = {
            "description": description,
            "rights": rights,
            "duties": duties,
            "sources": sources,
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }
        
        self.save_data()
        print(f"\n✅ '{name}' ölkəsi uğurla əlavə edildi!")
    
    def search_keyword(self):
        """Açar sözə görə axtar"""
        keyword = input("\n🔎 Axtarış sözünü daxil edin: ").lower().strip()
        
        print(f"\n'{keyword}' üçün nəticələr:")
        print("-"*50)
        
        found = False
        for country_name, data in self.countries.items():
            
            matching_rights = [r for r in data['rights'] if keyword in r.lower()]
            
            matching_duties = [d for d in data['duties'] if keyword in d.lower()]
            
            if matching_rights or matching_duties:
                found = True
                print(f"\n📌 {country_name}:")
                
                if matching_rights:
                    print("  Hüquqlar:")
                    for right in matching_rights:
                        print(f"    • {right}")
                
                if matching_duties:
                    print("  Vəzifələr:")
                    for duty in matching_duties:
                        print(f"    • {duty}")
        
        if not found:
            print("❌ Heç bir nəticə tapılmadı.")
    
    def run(self):
        """Əsas proqram dövrü"""
        while True:
            print("\n" + "="*60)
            print("HÜQUQ VƏ VƏZİFƏLƏR MƏLUMAT SİSTEMİ")
            print("="*60)
            print("1. Ölkələri siyahıla")
            print("2. Ölkə məlumatlarını göstər")
            print("3. Yeni ölkə əlavə et")
            print("4. Açar sözə görə axtar")
            print("5. Çıxış")
            print("="*60)
            
            choice = input("Seçiminiz (1-5): ").strip()
            
            if choice == "1":
                self.list_countries()
            elif choice == "2":
                self.list_countries()
                country = input("\nÖlkə adını daxil edin: ").strip()
                self.show_country_info(country)
            elif choice == "3":
                self.add_country()
            elif choice == "4":
                self.search_keyword()
            elif choice == "5":
                print("\n✨ Proqramdan çıxılır... Sağ olun!")
                break
            else:
                print("\n❌ Yanlış seçim! 1-5 arası rəqəm daxil edin.")
            
            input("\n🔽 Davam etmək üçün Enter düyməsini basın...")


if __name__ == "__main__":
    app = CountryRightsApp()
    app.run()
