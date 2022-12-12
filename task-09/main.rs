fn main() {
    let response = reqwest::blocking::get("https://crypto.com/price")
        .unwrap()
        .text()
        .unwrap();

    let document = scraper::Html::parse_document(&response);
    let crypto_selector = scraper::Selector::parse("tr.css-1cxc880").unwrap();

    let crypto_name_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let crypto_price_selector = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let crypto_24hr_change_selector = scraper::Selector::parse("td.css-1b7j986").unwrap();
    let crypto_24hr_vol_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let crypto_marketcap_selector = scraper::Selector::parse("td.css-1nh9lk8+td.css-1nh9lk8").unwrap();

    let mut wtr = csv::Writer::from_path("krypto.csv").unwrap();

    wtr.write_record(&["Krypto Name","Krypto Price","Krypto 24H Change","Krypto 24H Volume", "Krypto Marketcap"]).unwrap();

    for element in document.select(&crypto_selector) {
        let crypto_name_element = element.select(&crypto_name_selector).next().expect("Could not load the crypto");
     
        let crypto_name = crypto_name_element.text().collect::<String>();
        let crypto_price_element = element.select(&crypto_price_selector).next().expect("Could not load the price");
        let crypto_price = crypto_price_element.text().collect::<String>();

        let crypto_24hr_change_element = element.select(&crypto_24hr_change_selector).next().expect("Could not load the 24 HR change");
        let crypto_24hr_change = crypto_24hr_change_element.text().collect::<String>();

        let crypto_24hr_vol_element = element.select(&crypto_24hr_vol_selector).next().expect("Could not load the 24 HR vol");
        let crypto_24hr_vol = crypto_24hr_vol_element.text().collect::<String>(); 

        let crypto_marketcap_element = element.select(&crypto_marketcap_selector).next().expect("Could not load the 24 HR vol");
        let crypto_marketcap = crypto_marketcap_element.text().collect::<String>(); 

        wtr.write_record([&crypto_name,&crypto_price,&crypto_24hr_change,&crypto_24hr_vol,&crypto_marketcap]).expect("Could not create Selector.");
        /*println!(
            "{}: {}: {}: {} : {}",
            crypto_name, crypto_price, crypto_24hr_change, crypto_24hr_vol, crypto_marketcap
        );*/
    }
    wtr.flush().expect("Could not close file");
    println! ("Done");
}
