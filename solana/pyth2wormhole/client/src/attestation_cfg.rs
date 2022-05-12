use std::{
    collections::HashMap,
    str::FromStr,
};

use serde::{
    de::Error,
    Deserialize,
    Deserializer,
    Serialize,
    Serializer,
};
use solana_program::pubkey::Pubkey;

/// Pyth2wormhole config specific to attestation requests
#[derive(Debug, Deserialize, Serialize, PartialEq)]
pub struct AttestationConfig {
    pub symbol_groups: Vec<SymbolGroup>,
}

#[derive(Debug, Deserialize, Serialize, PartialEq)]
pub struct SymbolGroup {
    pub group_name: String,
    /// Attestation conditions applied to all symbols in this group
    pub conditions: AttestationConditions,
    pub symbols: Vec<P2WSymbol>,
}

/// Spontaneous attestation triggers. Attestation is triggered if any
/// of the active conditions is met. Option<> fields can be
/// de-activated with None. All conditions are inactive by default.
#[derive(Clone, Default, Debug, Deserialize, Serialize, PartialEq)]
pub struct AttestationConditions {
    /// Baseline, unconditional attestation interval. Attestation is triggered if the specified interval elapsed since last attestation.
    #[serde(default)]
    pub min_interval_secs: Option<u64>,

    /// Trigger attestation if price changes by the specified percentage.
    #[serde(default)]
    pub price_changed_pct: Option<f64>,

    /// Trigger attestation if publish_time changes
    #[serde(default)]
    pub publish_time_changed: bool,
}

/// Config entry for a Pyth product + price pair
#[derive(Default, Debug, Deserialize, Serialize, PartialEq, Eq)]
pub struct P2WSymbol {
    /// User-defined human-readable name
    pub name: Option<String>,

    #[serde(
        deserialize_with = "pubkey_string_de",
        serialize_with = "pubkey_string_ser"
    )]
    pub product_addr: Pubkey,
    #[serde(
        deserialize_with = "pubkey_string_de",
        serialize_with = "pubkey_string_ser"
    )]
    pub price_addr: Pubkey,
}

impl ToString for P2WSymbol {
    fn to_string(&self) -> String {
        self.name
            .clone()
            .unwrap_or(format!("Unnamed product {}", self.product_addr))
    }
}

// Helper methods for strinigified SOL addresses

fn pubkey_string_ser<S>(k: &Pubkey, ser: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    ser.serialize_str(&k.to_string())
}

fn pubkey_string_de<'de, D>(de: D) -> Result<Pubkey, D::Error>
where
    D: Deserializer<'de>,
{
    let pubkey_string = String::deserialize(de)?;
    let pubkey = Pubkey::from_str(&pubkey_string).map_err(D::Error::custom)?;
    Ok(pubkey)
}

#[cfg(test)]
mod tests {
    use super::*;

    use solitaire::ErrBox;

    #[test]
    fn test_sanity() -> Result<(), ErrBox> {
        let fastbois = SymbolGroup {
            group_name: "fast bois".to_owned(),
            conditions: AttestationConditions {
                min_interval_secs: Some(5),
                ..Default::default()
            },
            symbols: vec![
                P2WSymbol {
                    name: Some("ETHUSD".to_owned()),
                    ..Default::default()
                },
                P2WSymbol {
                    name: Some("BTCUSD".to_owned()),
                    ..Default::default()
                },
            ],
        };

        let slowbois = SymbolGroup {
            group_name: "slow bois".to_owned(),
            conditions: AttestationConditions {
                min_interval_secs: Some(200),
                ..Default::default()
            },
            symbols: vec![
                P2WSymbol {
                    name: Some("CNYAUD".to_owned()),
                    ..Default::default()
                },
                P2WSymbol {
                    name: Some("INRPLN".to_owned()),
                    ..Default::default()
                },
            ],
        };

        let cfg = AttestationConfig {
            symbol_groups: vec![fastbois, slowbois],
        };

        let serialized = serde_yaml::to_string(&cfg)?;

        let deserialized: AttestationConfig = serde_yaml::from_str(&serialized)?;

        assert_eq!(cfg, deserialized);

        Ok(())
    }
}
