# Specifikacija aplikacije za izvanmrežni rad u knjižnici

## 1. Pregled projekta

### 1.1 Ciljevi projekta
- Stvoriti sveobuhvatan sustav upravljanja knjižnicom s potpunom izvanmrežnom funkcionalnošću
- Implementirati robustan mehanizam sinkronizacije za nesmetan prijelaz između online i izvanmrežnog načina rada
- Pružiti intuitivno korisničko iskustvo za upravljanje osobnim i dijeljenim knjižnicama
- Osigurati integritet podataka na više uređaja i platformi
- Podržati kompatibilnost između različitih platformi (web, stolna računala i mobilni uređaji)

### 1.2 Komponente sustava
- **Sloj lokalne pohrane**: SQLite za izvorne aplikacije, IndexedDB za aplikacije temeljene na pregledniku
- **Modul sinkronizacije**: Mehanizam sinkronizacije u pozadini s rješavanjem sukoba
- **API sloj**: RESTful krajnje točke za komunikaciju s poslužiteljem
- **Korisničko sučelje**: Responzivni dizajn s pristupom koji je prvi na izvanmrežnom radu
- **Modul za autentifikaciju**: Podrška za izvanmrežnu autentifikaciju i autorizaciju

## 2. Funkcionalna specifikacija

### 2.1 Osnovne značajke

#### Upravljanje knjižnicom
- Katalogizacija knjiga s opsežnim metapodacima (naslov, autor, ISBN, datum objave, žanr itd.)
- Organizacija zbirke s prilagođenim policama i oznakama
- Napredno pretraživanje i mogućnosti filtriranja koje rade izvan mreže
- Povijest čitanja i praćenje napretka
- Sustav posudbe s podsjetnicima na datume dospijeća
#### Upravljanje korisnicima
- Korisnički profili s postavkama čitanja
- Ciljevi i postignuća čitanja
- Društvene značajke (recenzije, preporuke) koje se sinkroniziraju kada su online
- Administratorske mogućnosti za dijeljene/institucionalne knjižnice

#### Mogućnosti izvan mreže
- Potpuni pristup svim funkcijama knjižnice bez internetske veze
- Unos i izmjena podataka izvan mreže
- Funkcija pretraživanja i pregledavanja u predmemoriji
- Sadržaj medija izvan mreže (naslovnice knjiga, pregledi)
- Statistika i analitika čitanja u izvanmrežnom načinu rada
- Mogućnosti izvoza/uvoza za potrebe sigurnosne kopije

#### Značajke sinkronizacije
- Sinkronizacija u pozadini kada je veza dostupna
- Selektivne opcije sinkronizacije za upravljanje propusnošću
- Strategije rješavanja sukoba s korisnički definiranim postavkama
- Pokazatelji statusa sinkronizacije i povijest
- Sinkronizacija temeljena na prioritetu za kritične podatke

### 2.2 Proširene značajke
- Integracija s vanjskim bazama podataka o knjigama (Google knjige, Open Library)
- Integracija čitača e-knjiga
- Preporuke za čitanje na temelju sadržaja knjižnice
- Vizualizacija podataka za navike čitanja i sastav knjižnice
- Mogućnosti dijeljenja popisa za čitanje i preporuka

## 3. Tehnička specifikacija

### 3.1 Dizajn baze podataka

#### SQLite shema (izvorne aplikacije)
```sql
CREATE TABLE Knjige (
id_knjige TEKST PRIMARY KEY,
naslov TEKST NIJE NULL,
autor TEKST,
isbn TEKST,
datum_objave TEKST,
izdavač TEKST,
žanr TEKST,
opis TEKST,
slika_naslovnice BLOB,
datum_dodavanja TEKST NIJE NULL,
datum_modifikacije TEKST NIJE NULL,
status_sync_status INTEGER DEFAULT 0
);

CREATE TABLE Kolekcije (
id_kolekcije TEKST PRIMARY KEY,
naziv TEKST NIJE NULL,
opis TEKST,
datum_kreacije TEKST NIJE NULL,
datum_modifikacije TEKST NIJE NULL,
status_sync_status INTEGER DEFAULT 0
);

STVORI TABLICU Zbirke_knjiga (
id_knjige TEKST,
id_kolekcije TEKST,
datum_dodavanja TEKST NIJE NULL,
PRIMARNI KLJUČ (id_knjige, id_kolekcije),
STRANI KLJUČ (id_knjige) REFERENCE Knjige(id_knjige),
STRANI KLJUČ (id_kolekcije) REFERENCE Kolekcije(id_kolekcije)
);

STVORI TABLICU Napredak_čitanja (
progress_id TEKST PRIMARNI KLJUČ,
id_knjige TEKST,
korisnički_id TEKST,
broj_stranice CIJELI BROJ,
postotak REALAN,
datum_zadnjeg_čitanja TEKST NIJE NULL,
bilješke TEKST,
status_sinkronizacije CIJELI BROJ ZADANO 0,
STRANI KLJUČ (id_knjige) REFERENCE Knjige(id_knjige)
);

STVORI TABLICU LoanRecords (
id_knjige TEKST PRIMARNI KLJUČ,
id_knjige TEKST,
ime_posuđivača TEKST NIJE NULL,
kontakt_posuđivača TEKST,
datum_knjige TEKST NIJE NULL,
datum_dospijeća TEKST,
datum_povrata TEKST,
status TEKST NIJE NULL,
status_sync INTEGER DEFAULT 0,
STRANI KLJUČ (id_knjige) REFERENCE Knjige(id_knjige)
);

STVORI TABLICU SyncLog (
id_dnevnika INTEGER PRIMARNI KLJUČ AUTOINCREMENT,
vrsta_entiteta TEKST NIJE NULL,
id_entiteta TEKST NIJE NULL,
vrsta_akcije TEKST NIJE NULL,
vremenska_oznaka TEKST NIJE NULL,
status TEKST NIJE NULL
);
```

#### IndexedDB shema (aplikacije temeljene na pregledniku)
```javascript
// Trgovina knjigama

keyPath: "book_id",
indexes: [
{ name: "title", keyPath: "title", options: { unique: false } },
{ name: "author", keyPath: "author", options: { unique: false } },
{ name: "isbn", keyPath: "isbn", options: { unique: true } },
{ name: "žanr", keyPath: "žanr", options: { unique: false } },
{ name: "sync_status", keyPath: "sync_status", options: { unique: false } }
]
}

// Trgovina zbirki

keyPath: "collection_id",
indexes: [
{ name: "name", keyPath: "name", options: { unique: true } },
{ name: "sync_status", keyPath: "sync_status", options: { unique: false } }
]
}

// Trgovina kolekcija knjiga
{
keyPath: ["id_knjige", "id_kolekcije"],
indexes: [
{ name: "id_knjige",
