import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in!')
    print(f'Bot is connected to {len(bot.guilds)} server(s)')
    await bot.change_presence(activity=discord.Game(name="!help for 40+ agent commands"))

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # Process commands
    await bot.process_commands(message)

# ============================================================================
# BASIC COMMANDS
# ============================================================================

@bot.command(name='hello', help='Greets the user')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

@bot.command(name='ping', help='Check bot latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Latency: {latency}ms')

@bot.command(name='info', help='Get bot information')
async def info(ctx):
    embed = discord.Embed(
        title="ProjectTime Agent Bot",
        description="Discord Bot with 40+ Agent Commands",
        color=discord.Color.blue()
    )
    embed.add_field(name="Server Count", value=len(bot.guilds), inline=True)
    embed.add_field(name="Latency", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="Total Agents", value="40+", inline=True)
    embed.add_field(name="Categories", value="Master, Trading, Research, Macro, Market, Quant, Risk, Privacy, Infrastructure, Info", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='agents', help='List all available agent categories')
async def agents(ctx):
    embed = discord.Embed(
        title="Available Agent Categories",
        description="Use !help <category> for specific commands",
        color=discord.Color.green()
    )
    embed.add_field(name="Master Agents", value="!hoags, !moneybags", inline=False)
    embed.add_field(name="Trading Agents", value="!equities, !options, !convertible, !investment_banker", inline=False)
    embed.add_field(name="Research Agents", value="!valuation, !research, !portfolio", inline=False)
    embed.add_field(name="Macro Agents", value="!economist, !fed, !treasuries, !global_macro, !central_banker", inline=False)
    embed.add_field(name="Market Agents", value="!market_psych, !market_dynamics, !market_liquidity, !game_theorist", inline=False)
    embed.add_field(name="Quant Agents", value="!alt_data, !momentum, !unusual_activity", inline=False)
    embed.add_field(name="Risk Agents", value="!risk, !pair_trader", inline=False)
    embed.add_field(name="Privacy Agents", value="!digital_privacy, !financial_privacy, !social_privacy, !counter_surveillance, !biometric", inline=False)
    embed.add_field(name="Infrastructure Agents", value="!compliance, !foundation, !onboarding, !operations, !qa_security, !technology", inline=False)
    embed.add_field(name="Info Agents", value="!capital_raising, !investor_relations, !news, !vcpe", inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# MASTER AGENTS
# ============================================================================

@bot.command(name='hoags', help='HoagsAgent - Master Controller operations')
async def hoags(ctx, operation: str = "network_overview"):
    """HoagsAgent commands: network_overview, issue_directive, algorithm_status, ico_strategy"""
    embed = discord.Embed(title="HoagsAgent", color=discord.Color.purple())
    
    if operation == "network_overview":
        embed.add_field(name="Network Overview", value="Master controller of 40+ agents", inline=False)
        embed.add_field(name="Subordinate Agents", value="40+", inline=True)
        embed.add_field(name="ML Protocols", value="All 6 protocols active", inline=True)
        embed.add_field(name="Status", value="Active", inline=True)
    elif operation == "issue_directive":
        embed.add_field(name="Directive Issued", value="Strategic directive sent to agents", inline=False)
    elif operation == "algorithm_status":
        embed.add_field(name="Algorithm Development", value="Multiple strategies in pipeline", inline=False)
    elif operation == "ico_strategy":
        embed.add_field(name="ICO Strategy", value="Multi-phase protocol launch plan", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='moneybags', help='MoneybagsAgent - Algorithm Training operations')
async def moneybags(ctx, operation: str = "synthesize"):
    """MoneybagsAgent commands: synthesize, ingest, insights, report, feed_hoags"""
    embed = discord.Embed(title="MoneybagsAgent", color=discord.Color.gold())
    
    if operation == "synthesize":
        embed.add_field(name="Synthesis", value="Processing training data from all sources", inline=False)
        embed.add_field(name="Documents", value="Scanning training materials", inline=True)
        embed.add_field(name="Patterns", value="Extracting algorithmic patterns", inline=True)
    elif operation == "ingest":
        embed.add_field(name="Document Ingestion", value="Reading training materials and ICO data", inline=False)
    elif operation == "insights":
        embed.add_field(name="Algorithm Insights", value="Generating trading strategy insights", inline=False)
    elif operation == "report":
        embed.add_field(name="Excel Report", value="Creating algorithm training output report", inline=False)
    elif operation == "feed_hoags":
        embed.add_field(name="HoagsAgent Feed", value="Sending synthesized data to master", inline=False)
    
    await ctx.send(embed=embed)

# ============================================================================
# TRADING AGENTS
# ============================================================================

@bot.command(name='equities', help='EquitiesTraderAgent - Cash equities operations')
async def equities(ctx, operation: str = "rebalance", *, args: str = ""):
    """Equities commands: rebalance, exposure_check, order_staging"""
    embed = discord.Embed(title="EquitiesTraderAgent", color=discord.Color.blue())
    
    if operation == "rebalance":
        embed.add_field(name="Rebalance Plan", value="Generating rebalance orders", inline=False)
        embed.add_field(name="Target Cash", value="5%", inline=True)
        embed.add_field(name="Orders", value="Multiple positions", inline=True)
    elif operation == "exposure_check":
        embed.add_field(name="Exposure Check", value="Checking portfolio exposures", inline=False)
        embed.add_field(name="Gross", value="1.8x", inline=True)
        embed.add_field(name="Net", value="0.45x", inline=True)
    elif operation == "order_staging":
        embed.add_field(name="Order Staging", value="Preparing orders for execution", inline=False)
        embed.add_field(name="Destination", value="IBKR", inline=True)
        embed.add_field(name="Algorithm", value="VWAP", inline=True)
    
    await ctx.send(embed=embed)

@bot.command(name='options', help='OptionsTraderAgent - Options operations')
async def options(ctx, operation: str = "greeks", *, args: str = ""):
    """Options commands: greeks, strategy_builder, hedge_recommendation"""
    embed = discord.Embed(title="OptionsTraderAgent", color=discord.Color.orange())
    
    if operation == "greeks":
        ticker = args.split()[0] if args else "SPY"
        embed.add_field(name=f"Greeks Dashboard - {ticker}", value="Options Greeks analysis", inline=False)
        embed.add_field(name="Delta", value="0.32", inline=True)
        embed.add_field(name="Gamma", value="0.015", inline=True)
        embed.add_field(name="Theta", value="-12000", inline=True)
        embed.add_field(name="Vega", value="45000", inline=True)
    elif operation == "strategy_builder":
        embed.add_field(name="Strategy Builder", value="Building options strategy", inline=False)
        embed.add_field(name="Structure", value="Collar", inline=True)
    elif operation == "hedge":
        embed.add_field(name="Hedge Recommendation", value="Tail risk hedge suggestion", inline=False)
        embed.add_field(name="Trade", value="SPX put spread", inline=True)
        embed.add_field(name="Cost", value="35 bps", inline=True)
    
    await ctx.send(embed=embed)

@bot.command(name='convertible', help='ConvertibleTraderAgent operations')
async def convertible(ctx, operation: str = "arb_scan"):
    """Convertible commands: arb_scan, hedge_plan, liquidity_check"""
    embed = discord.Embed(title="ConvertibleTraderAgent", color=discord.Color.teal())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='investment_banker', help='InvestmentBankerAgent operations')
async def investment_banker(ctx, operation: str = "mna"):
    """Investment Banker commands: mna_analysis, precedent_review, lbo_outline"""
    embed = discord.Embed(title="InvestmentBankerAgent", color=discord.Color.dark_blue())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# RESEARCH AGENTS
# ============================================================================

@bot.command(name='valuation', help='ValuationAgent - Hogan Model DCF')
async def valuation(ctx, ticker: str = "AAPL", *, args: str = ""):
    """Valuation using Hogan Model. Usage: !valuation <ticker>"""
    embed = discord.Embed(title=f"ValuationAgent - {ticker}", color=discord.Color.green())
    embed.add_field(name="Model", value="Hogan Model DCF", inline=False)
    embed.add_field(name="Owner Earnings", value="Calculated with SBC deduction", inline=False)
    embed.add_field(name="Margin of Safety", value="30% required", inline=True)
    embed.add_field(name="Recommendation", value="BUY/PASS", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='research', help='ResearchProcessAgent operations')
async def research(ctx, operation: str = "thesis"):
    """Research commands: research_db_update, thesis_scorecard, kill_box_review"""
    embed = discord.Embed(title="ResearchProcessAgent", color=discord.Color.green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='portfolio', help='PortfolioManagementAgent operations')
async def portfolio(ctx, operation: str = "exposure"):
    """Portfolio commands: exposure_snapshot, pnl_attribution, rebalance_plan"""
    embed = discord.Embed(title="PortfolioManagementAgent", color=discord.Color.green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# MACRO AGENTS
# ============================================================================

@bot.command(name='economist', help='EconomistAgent - Macroeconomic analysis')
async def economist(ctx, operation: str = "outlook"):
    """Economist commands: macro_outlook, indicator_analysis"""
    embed = discord.Embed(title="EconomistAgent", color=discord.Color.red())
    
    if operation == "outlook":
        embed.add_field(name="Macro Outlook", value="Economic forecast", inline=False)
        embed.add_field(name="GDP Forecast", value="2.3% (2025)", inline=True)
        embed.add_field(name="Inflation", value="2.8% (2025)", inline=True)
        embed.add_field(name="Recession Prob", value="25%", inline=True)
    elif operation == "indicators":
        embed.add_field(name="Economic Indicators", value="Leading, coincident, lagging", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='fed', help='FedWhispererAgent - Fed rate analysis')
async def fed(ctx, operation: str = "forecast"):
    """Fed commands: rate_forecast, fomc_analysis"""
    embed = discord.Embed(title="FedWhispererAgent", color=discord.Color.red())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='treasuries', help='TreasuriesAgent - Yield curve analysis')
async def treasuries(ctx, operation: str = "yield_curve"):
    """Treasuries commands: yield_curve, duration_analysis"""
    embed = discord.Embed(title="TreasuriesAgent", color=discord.Color.red())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='global_macro', help='GlobalMacroAgent operations')
async def global_macro(ctx, operation: str = "overview"):
    """Global Macro commands: global_overview, fx_analysis"""
    embed = discord.Embed(title="GlobalMacroAgent", color=discord.Color.red())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='central_banker', help='CentralBankerAgent operations')
async def central_banker(ctx, operation: str = "rates"):
    """Central Banker commands: global_rates"""
    embed = discord.Embed(title="CentralBankerAgent", color=discord.Color.red())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# MARKET AGENTS
# ============================================================================

@bot.command(name='market_psych', help='MarketPsychologistAgent - Sentiment analysis')
async def market_psych(ctx, operation: str = "sentiment"):
    """Market Psych commands: sentiment_analysis, behavioral_biases"""
    embed = discord.Embed(title="MarketPsychologistAgent", color=discord.Color.purple())
    
    if operation == "sentiment":
        embed.add_field(name="Sentiment Analysis", value="Market psychology metrics", inline=False)
        embed.add_field(name="Fear/Greed Index", value="65", inline=True)
        embed.add_field(name="VIX", value="14.5", inline=True)
        embed.add_field(name="Overall Sentiment", value="Cautiously Optimistic", inline=True)
    elif operation == "biases":
        embed.add_field(name="Behavioral Biases", value="Crowding and contrarian signals", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='market_dynamics', help='MarketDynamicsAgent operations')
async def market_dynamics(ctx, operation: str = "regime"):
    """Market Dynamics commands: market_regime, sector_rotation"""
    embed = discord.Embed(title="MarketDynamicsAgent", color=discord.Color.purple())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='market_liquidity', help='MarketLiquidityAgent operations')
async def market_liquidity(ctx, operation: str = "score"):
    """Market Liquidity commands: liquidity_score, portfolio_liquidity"""
    embed = discord.Embed(title="MarketLiquidityAgent", color=discord.Color.purple())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='game_theorist', help='GameTheoristAgent operations')
async def game_theorist(ctx, operation: str = "competitive"):
    """Game Theorist commands: competitive_analysis, activist_analysis"""
    embed = discord.Embed(title="GameTheoristAgent", color=discord.Color.purple())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# QUANT AGENTS
# ============================================================================

@bot.command(name='alt_data', help='AlternativeDataAgent - Non-traditional data')
async def alt_data(ctx, operation: str = "analyze", *, args: str = ""):
    """Alt Data commands: analyze_alt_data, satellite_data, web_traffic, sentiment_analysis"""
    embed = discord.Embed(title="AlternativeDataAgent", color=discord.Color.blue())
    
    ticker = args.split()[0] if args else "AAPL"
    if operation == "analyze":
        embed.add_field(name=f"Alt Data Analysis - {ticker}", value="Non-traditional data sources", inline=False)
        embed.add_field(name="Sources", value="Satellite, web traffic, credit cards", inline=False)
        embed.add_field(name="Signal", value="Bullish", inline=True)
        embed.add_field(name="Confidence", value="75%", inline=True)
    elif operation == "satellite":
        embed.add_field(name="Satellite Data", value="Parking lot fill rate analysis", inline=False)
    elif operation == "web_traffic":
        embed.add_field(name="Web Traffic", value="Monthly visits analysis", inline=False)
    elif operation == "sentiment":
        embed.add_field(name="Sentiment Analysis", value="Social and news sentiment", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='momentum', help='MomentumSignalsAgent operations')
async def momentum(ctx, operation: str = "screen"):
    """Momentum commands: screen_momentum, time_series, cross_sectional"""
    embed = discord.Embed(title="MomentumSignalsAgent", color=discord.Color.blue())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='unusual_activity', help='UnusualActivityAgent operations')
async def unusual_activity(ctx, operation: str = "scan"):
    """Unusual Activity commands: scan_unusual, options_flow, dark_pool"""
    embed = discord.Embed(title="UnusualActivityAgent", color=discord.Color.blue())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# RISK AGENTS
# ============================================================================

@bot.command(name='risk', help='RiskManagementAgent operations')
async def risk(ctx, operation: str = "var"):
    """Risk commands: var_run, stress_test, correlation_matrix"""
    embed = discord.Embed(title="RiskManagementAgent", color=discord.Color.dark_red())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='pair_trader', help='PairTraderAgent operations')
async def pair_trader(ctx, operation: str = "scan"):
    """Pair Trader commands: pair_scan, signal_monitor, backtest"""
    embed = discord.Embed(title="PairTraderAgent", color=discord.Color.dark_red())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# PRIVACY AGENTS
# ============================================================================

@bot.command(name='digital_privacy', help='DigitalPrivacyAgent operations')
async def digital_privacy(ctx, operation: str = "footprint"):
    """Digital Privacy commands: footprint_scan, broker_removal, metadata_scrub, dark_web_scan, identity_obfuscate"""
    embed = discord.Embed(title="DigitalPrivacyAgent", color=discord.Color.dark_grey())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='financial_privacy', help='FinancialPrivacyAgent operations')
async def financial_privacy(ctx, operation: str = "audit"):
    """Financial Privacy commands: privacy_audit, structure_design, transaction_privacy, crypto_privacy, net_worth_obfuscation"""
    embed = discord.Embed(title="FinancialPrivacyAgent", color=discord.Color.dark_grey())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='social_privacy', help='SocialPrivacyAgent operations')
async def social_privacy(ctx, operation: str = "vulnerability"):
    """Social Privacy commands: vulnerability_assessment, se_defense_training, relationship_audit, public_records_cleanup, inner_circle_protection"""
    embed = discord.Embed(title="SocialPrivacyAgent", color=discord.Color.dark_grey())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='counter_surveillance', help='CounterSurveillanceAgent operations')
async def counter_surveillance(ctx, operation: str = "threat"):
    """Counter Surveillance commands: threat_assessment, tscm_sweep, physical_detection, secure_comms, location_privacy"""
    embed = discord.Embed(title="CounterSurveillanceAgent", color=discord.Color.dark_grey())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='biometric', help='BiometricCountermeasuresAgent operations')
async def biometric(ctx, operation: str = "vulnerability"):
    """Biometric commands: vulnerability_scan, facial_countermeasures, voice_protection, database_removal, camera_avoidance"""
    embed = discord.Embed(title="BiometricCountermeasuresAgent", color=discord.Color.dark_grey())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# INFRASTRUCTURE AGENTS
# ============================================================================

@bot.command(name='compliance', help='ComplianceAgent operations')
async def compliance(ctx, operation: str = "check"):
    """Compliance commands: compliance_check, regulatory_monitor"""
    embed = discord.Embed(title="ComplianceAgent", color=discord.Color.dark_green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='foundation', help='FoundationAgent operations')
async def foundation(ctx, operation: str = "setup"):
    """Foundation commands: foundation_setup"""
    embed = discord.Embed(title="FoundationAgent", color=discord.Color.dark_green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='onboarding', help='OnboardingAgent operations')
async def onboarding(ctx, operation: str = "onboard"):
    """Onboarding commands: onboard_user"""
    embed = discord.Embed(title="OnboardingAgent", color=discord.Color.dark_green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='operations', help='OperationsAgent operations')
async def operations(ctx, operation: str = "monitor"):
    """Operations commands: operations_monitor"""
    embed = discord.Embed(title="OperationsAgent", color=discord.Color.dark_green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='qa_security', help='QASecurityAgent operations')
async def qa_security(ctx, operation: str = "security_check"):
    """QA Security commands: security_check, quality_assurance"""
    embed = discord.Embed(title="QASecurityAgent", color=discord.Color.dark_green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='technology', help='TechnologyAgent operations')
async def technology(ctx, operation: str = "health"):
    """Technology commands: script_health, log_rotation, documentation_sync"""
    embed = discord.Embed(title="TechnologyAgent", color=discord.Color.dark_green())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# INFO AGENTS
# ============================================================================

@bot.command(name='capital_raising', help='CapitalRaisingAgent operations')
async def capital_raising(ctx, operation: str = "raise"):
    """Capital Raising commands: capital_raise"""
    embed = discord.Embed(title="CapitalRaisingAgent", color=discord.Color.cyan())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='investor_relations', help='InvestorRelationsAgent operations')
async def investor_relations(ctx, operation: str = "relations"):
    """Investor Relations commands: investor_relations"""
    embed = discord.Embed(title="InvestorRelationsAgent", color=discord.Color.cyan())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='news', help='NewsAnalystAgent operations')
async def news(ctx, operation: str = "analyze"):
    """News commands: news_analysis"""
    embed = discord.Embed(title="NewsAnalystAgent", color=discord.Color.cyan())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='vcpe', help='VCPEAnalystAgent operations')
async def vcpe(ctx, operation: str = "analyze"):
    """VCPE commands: vcpe_analysis"""
    embed = discord.Embed(title="VCPEAnalystAgent", color=discord.Color.cyan())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# ============================================================================
# TAX AGENTS
# ============================================================================

@bot.command(name='tax_equities', help='TaxEquitiesAgent operations')
async def tax_equities(ctx, operation: str = "tax"):
    """Tax Equities commands: tax_analysis"""
    embed = discord.Embed(title="TaxEquitiesAgent", color=discord.Color.dark_orange())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='tax_options', help='TaxOptionsAgent operations')
async def tax_options(ctx, operation: str = "tax"):
    """Tax Options commands: tax_analysis"""
    embed = discord.Embed(title="TaxOptionsAgent", color=discord.Color.dark_orange())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='accounting', help='AccountingAgent operations')
async def accounting(ctx, operation: str = "accounting"):
    """Accounting commands: accounting_analysis"""
    embed = discord.Embed(title="AccountingAgent", color=discord.Color.dark_orange())
    embed.add_field(name="Operation", value=operation, inline=False)
    await ctx.send(embed=embed)

# Run the bot
if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: DISCORD_TOKEN not found in environment variables!")
        print("Please create a .env file with DISCORD_TOKEN=your_token_here")
    else:
        bot.run(token)
