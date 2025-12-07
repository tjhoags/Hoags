# Discord Bot - ProjectTime Agent Network

A comprehensive Discord bot with commands for all 40+ agents in the ProjectTime Agent Framework.

## Features

- **40+ Agent Commands** - Access all specialized agents through Discord
- **Organized by Category** - Commands grouped by agent specialization
- **Real-time Responses** - Get instant agent insights and analysis
- **Easy to Use** - Simple command syntax with help system

## Setup

1. Install Python 3.8 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```
DISCORD_TOKEN=your_discord_bot_token_here
```

4. Get your Discord bot token:
   - Go to https://discord.com/developers/applications
   - Create a new application or select an existing one
   - Go to the "Bot" section
   - Copy the token and add it to your `.env` file

5. Invite the bot to your server:
   - In the Discord Developer Portal, go to OAuth2 > URL Generator
   - Select "bot" scope
   - Select necessary permissions (Send Messages, Read Messages, etc.)
   - Copy the generated URL and open it in your browser
   - Select your server and authorize

6. Run the bot:
```bash
python bot.py
```

## Commands

### Basic Commands
- `!hello` - Greets the user
- `!ping` - Check bot latency
- `!info` - Get bot information
- `!agents` - List all available agent categories
- `!help` - Show all available commands

### Master Agents
- `!hoags [operation]` - HoagsAgent (Master Controller)
  - Operations: network_overview, issue_directive, algorithm_status, ico_strategy
- `!moneybags [operation]` - MoneybagsAgent (Algorithm Training)
  - Operations: synthesize, ingest, insights, report, feed_hoags

### Trading Agents
- `!equities [operation]` - EquitiesTraderAgent
  - Operations: rebalance, exposure_check, order_staging
- `!options [operation]` - OptionsTraderAgent
  - Operations: greeks, strategy_builder, hedge
- `!convertible [operation]` - ConvertibleTraderAgent
  - Operations: arb_scan, hedge_plan, liquidity_check
- `!investment_banker [operation]` - InvestmentBankerAgent
  - Operations: mna, precedent_review, lbo_outline

### Research Agents
- `!valuation [ticker]` - ValuationAgent (Hogan Model DCF)
- `!research [operation]` - ResearchProcessAgent
  - Operations: research_db_update, thesis_scorecard, kill_box_review
- `!portfolio [operation]` - PortfolioManagementAgent
  - Operations: exposure_snapshot, pnl_attribution, rebalance_plan

### Macro Agents
- `!economist [operation]` - EconomistAgent
  - Operations: outlook, indicators
- `!fed [operation]` - FedWhispererAgent
  - Operations: forecast, fomc_analysis
- `!treasuries [operation]` - TreasuriesAgent
  - Operations: yield_curve, duration_analysis
- `!global_macro [operation]` - GlobalMacroAgent
  - Operations: overview, fx_analysis
- `!central_banker [operation]` - CentralBankerAgent
  - Operations: rates

### Market Agents
- `!market_psych [operation]` - MarketPsychologistAgent
  - Operations: sentiment, biases
- `!market_dynamics [operation]` - MarketDynamicsAgent
  - Operations: regime, sector_rotation
- `!market_liquidity [operation]` - MarketLiquidityAgent
  - Operations: score, portfolio_liquidity
- `!game_theorist [operation]` - GameTheoristAgent
  - Operations: competitive, activist_analysis

### Quant Agents
- `!alt_data [operation] [ticker]` - AlternativeDataAgent
  - Operations: analyze, satellite_data, web_traffic, sentiment
- `!momentum [operation]` - MomentumSignalsAgent
  - Operations: screen, time_series, cross_sectional
- `!unusual_activity [operation]` - UnusualActivityAgent
  - Operations: scan, options_flow, dark_pool

### Risk Agents
- `!risk [operation]` - RiskManagementAgent
  - Operations: var, stress_test, correlation_matrix
- `!pair_trader [operation]` - PairTraderAgent
  - Operations: scan, signal_monitor, backtest

### Privacy Agents
- `!digital_privacy [operation]` - DigitalPrivacyAgent
  - Operations: footprint, broker_removal, metadata_scrub, dark_web_scan, identity_obfuscate
- `!financial_privacy [operation]` - FinancialPrivacyAgent
  - Operations: audit, structure_design, transaction_privacy, crypto_privacy, net_worth_obfuscation
- `!social_privacy [operation]` - SocialPrivacyAgent
  - Operations: vulnerability, se_defense_training, relationship_audit, public_records_cleanup, inner_circle_protection
- `!counter_surveillance [operation]` - CounterSurveillanceAgent
  - Operations: threat, tscm_sweep, physical_detection, secure_comms, location_privacy
- `!biometric [operation]` - BiometricCountermeasuresAgent
  - Operations: vulnerability, facial_countermeasures, voice_protection, database_removal, camera_avoidance

### Infrastructure Agents
- `!compliance [operation]` - ComplianceAgent
  - Operations: check, regulatory_monitor
- `!foundation [operation]` - FoundationAgent
  - Operations: setup
- `!onboarding [operation]` - OnboardingAgent
  - Operations: onboard
- `!operations [operation]` - OperationsAgent
  - Operations: monitor
- `!qa_security [operation]` - QASecurityAgent
  - Operations: security_check, quality_assurance
- `!technology [operation]` - TechnologyAgent
  - Operations: health, log_rotation, documentation_sync

### Info Agents
- `!capital_raising [operation]` - CapitalRaisingAgent
- `!investor_relations [operation]` - InvestorRelationsAgent
- `!news [operation]` - NewsAnalystAgent
- `!vcpe [operation]` - VCPEAnalystAgent

### Tax Agents
- `!tax_equities [operation]` - TaxEquitiesAgent
- `!tax_options [operation]` - TaxOptionsAgent
- `!accounting [operation]` - AccountingAgent

## Examples

```
!hoags network_overview
!equities rebalance
!options greeks SPY
!valuation AAPL
!economist outlook
!market_psych sentiment
!alt_data analyze AAPL
!risk var
```

## License

MIT
