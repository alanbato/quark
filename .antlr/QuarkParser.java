// Generated from /Users/ebarragan/Library/Mobile Documents/com~apple~CloudDocs/Tec de Monterrey/Compiladores/quark/Quark.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class QuarkParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, ID=35, TYPE_ID=36, CONST_I=37, CONST_F=38, 
		STRING=39, SPACE=40;
	public static final int
		RULE_function = 0, RULE_params = 1, RULE_moreparams = 2, RULE_moreTypes = 3, 
		RULE_typeRule = 4, RULE_typedef = 5, RULE_typeset = 6, RULE_cond = 7, 
		RULE_expression = 8, RULE_boolRule = 9, RULE_comparator = 10, RULE_exp = 11, 
		RULE_term = 12, RULE_more_expressions = 13, RULE_factor = 14, RULE_varconst = 15, 
		RULE_block = 16, RULE_statement = 17, RULE_func_call = 18, RULE_assignment = 19, 
		RULE_main = 20, RULE_things = 21, RULE_morethings = 22;
	public static final String[] ruleNames = {
		"function", "params", "moreparams", "moreTypes", "typeRule", "typedef", 
		"typeset", "cond", "expression", "boolRule", "comparator", "exp", "term", 
		"more_expressions", "factor", "varconst", "block", "statement", "func_call", 
		"assignment", "main", "things", "morethings"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'def'", "'('", "')'", "'->'", "'{'", "'}'", "'default {'", "':'", 
		"','", "'Int'", "'?'", "'Bool'", "'Float'", "'String'", "'non'", "'['", 
		"']'", "'type'", "'<-'", "'|'", "'True'", "'False'", "'>'", "'<'", "'='", 
		"'>='", "'<='", "'!='", "'+'", "'-'", "'*'", "'/'", "'%'", "'[]'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, "ID", 
		"TYPE_ID", "CONST_I", "CONST_F", "STRING", "SPACE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Quark.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public QuarkParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class FunctionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(QuarkParser.ID, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public TypeRuleContext typeRule() {
			return getRuleContext(TypeRuleContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<CondContext> cond() {
			return getRuleContexts(CondContext.class);
		}
		public CondContext cond(int i) {
			return getRuleContext(CondContext.class,i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(T__0);
			setState(47);
			match(ID);
			setState(48);
			match(T__1);
			setState(49);
			params();
			setState(50);
			match(T__2);
			setState(51);
			match(T__3);
			setState(52);
			typeRule();
			setState(53);
			match(T__4);
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(54);
				cond();
				setState(55);
				match(T__4);
				setState(56);
				block();
				setState(57);
				match(T__5);
				}
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(64);
			match(T__6);
			setState(65);
			block();
			setState(66);
			match(T__5);
			setState(67);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(QuarkParser.ID, 0); }
		public TypeRuleContext typeRule() {
			return getRuleContext(TypeRuleContext.class,0);
		}
		public MoreparamsContext moreparams() {
			return getRuleContext(MoreparamsContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_params);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(ID);
			setState(70);
			match(T__7);
			setState(71);
			typeRule();
			setState(72);
			moreparams();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MoreparamsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(QuarkParser.ID, 0); }
		public TypeRuleContext typeRule() {
			return getRuleContext(TypeRuleContext.class,0);
		}
		public MoreparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moreparams; }
	}

	public final MoreparamsContext moreparams() throws RecognitionException {
		MoreparamsContext _localctx = new MoreparamsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_moreparams);
		try {
			setState(79);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				match(T__8);
				setState(75);
				match(ID);
				setState(76);
				match(T__7);
				setState(77);
				typeRule();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MoreTypesContext extends ParserRuleContext {
		public TypeRuleContext typeRule() {
			return getRuleContext(TypeRuleContext.class,0);
		}
		public MoreTypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moreTypes; }
	}

	public final MoreTypesContext moreTypes() throws RecognitionException {
		MoreTypesContext _localctx = new MoreTypesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_moreTypes);
		try {
			setState(84);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				match(T__8);
				setState(82);
				typeRule();
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeRuleContext extends ParserRuleContext {
		public TypeRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeRule; }
	 
		public TypeRuleContext() { }
		public void copyFrom(TypeRuleContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FloatContext extends TypeRuleContext {
		public FloatContext(TypeRuleContext ctx) { copyFrom(ctx); }
	}
	public static class ListOfTypeContext extends TypeRuleContext {
		public TypeRuleContext typeRule() {
			return getRuleContext(TypeRuleContext.class,0);
		}
		public MoreTypesContext moreTypes() {
			return getRuleContext(MoreTypesContext.class,0);
		}
		public ListOfTypeContext(TypeRuleContext ctx) { copyFrom(ctx); }
	}
	public static class StringContext extends TypeRuleContext {
		public StringContext(TypeRuleContext ctx) { copyFrom(ctx); }
	}
	public static class BooleanContext extends TypeRuleContext {
		public BooleanContext(TypeRuleContext ctx) { copyFrom(ctx); }
	}
	public static class UserTypeContext extends TypeRuleContext {
		public TerminalNode TYPE_ID() { return getToken(QuarkParser.TYPE_ID, 0); }
		public UserTypeContext(TypeRuleContext ctx) { copyFrom(ctx); }
	}
	public static class NoneContext extends TypeRuleContext {
		public NoneContext(TypeRuleContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends TypeRuleContext {
		public IntContext(TypeRuleContext ctx) { copyFrom(ctx); }
	}

	public final TypeRuleContext typeRule() throws RecognitionException {
		TypeRuleContext _localctx = new TypeRuleContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_typeRule);
		int _la;
		try {
			setState(109);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TYPE_ID:
				_localctx = new UserTypeContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(86);
				match(TYPE_ID);
				}
				break;
			case T__9:
				_localctx = new IntContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				match(T__9);
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(88);
					match(T__10);
					}
				}

				}
				break;
			case T__11:
				_localctx = new BooleanContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(91);
				match(T__11);
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(92);
					match(T__10);
					}
				}

				}
				break;
			case T__12:
				_localctx = new FloatContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(95);
				match(T__12);
				setState(97);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(96);
					match(T__10);
					}
				}

				}
				break;
			case T__13:
				_localctx = new StringContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(99);
				match(T__13);
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(100);
					match(T__10);
					}
				}

				}
				break;
			case T__14:
				_localctx = new NoneContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(103);
				match(T__14);
				}
				break;
			case T__15:
				_localctx = new ListOfTypeContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(104);
				match(T__15);
				setState(105);
				typeRule();
				setState(106);
				moreTypes();
				setState(107);
				match(T__16);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedefContext extends ParserRuleContext {
		public TerminalNode TYPE_ID() { return getToken(QuarkParser.TYPE_ID, 0); }
		public TypeRuleContext typeRule() {
			return getRuleContext(TypeRuleContext.class,0);
		}
		public TypesetContext typeset() {
			return getRuleContext(TypesetContext.class,0);
		}
		public TypedefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedef; }
	}

	public final TypedefContext typedef() throws RecognitionException {
		TypedefContext _localctx = new TypedefContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_typedef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(T__17);
			setState(112);
			match(TYPE_ID);
			setState(113);
			match(T__18);
			setState(116);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case TYPE_ID:
				{
				setState(114);
				typeRule();
				}
				break;
			case T__1:
				{
				setState(115);
				typeset();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypesetContext extends ParserRuleContext {
		public List<TypeRuleContext> typeRule() {
			return getRuleContexts(TypeRuleContext.class);
		}
		public TypeRuleContext typeRule(int i) {
			return getRuleContext(TypeRuleContext.class,i);
		}
		public TypesetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeset; }
	}

	public final TypesetContext typeset() throws RecognitionException {
		TypesetContext _localctx = new TypesetContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_typeset);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(T__1);
			setState(119);
			typeRule();
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__19) {
				{
				{
				setState(120);
				match(T__19);
				setState(121);
				typeRule();
				}
				}
				setState(126);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(127);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public More_expressionsContext more_expressions() {
			return getRuleContext(More_expressionsContext.class,0);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_cond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(T__1);
			setState(130);
			expression(0);
			setState(131);
			more_expressions();
			setState(132);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public BoolRuleContext boolRule() {
			return getRuleContext(BoolRuleContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public ComparatorContext comparator() {
			return getRuleContext(ComparatorContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(135);
				boolRule();
				}
				break;
			case 2:
				{
				setState(136);
				exp();
				setState(137);
				expression(5);
				}
				break;
			case 3:
				{
				setState(139);
				exp();
				}
				break;
			case 4:
				{
				setState(140);
				match(T__14);
				}
				break;
			case 5:
				{
				setState(141);
				func_call();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(150);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(144);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(145);
					comparator();
					setState(146);
					expression(4);
					}
					} 
				}
				setState(152);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BoolRuleContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(QuarkParser.ID, 0); }
		public BoolRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolRule; }
	}

	public final BoolRuleContext boolRule() throws RecognitionException {
		BoolRuleContext _localctx = new BoolRuleContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_boolRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__21) | (1L << ID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComparatorContext extends ParserRuleContext {
		public ComparatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparator; }
	 
		public ComparatorContext() { }
		public void copyFrom(ComparatorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class GreaterEqualContext extends ComparatorContext {
		public GreaterEqualContext(ComparatorContext ctx) { copyFrom(ctx); }
	}
	public static class LesserContext extends ComparatorContext {
		public LesserContext(ComparatorContext ctx) { copyFrom(ctx); }
	}
	public static class NotEqualContext extends ComparatorContext {
		public NotEqualContext(ComparatorContext ctx) { copyFrom(ctx); }
	}
	public static class EqualContext extends ComparatorContext {
		public EqualContext(ComparatorContext ctx) { copyFrom(ctx); }
	}
	public static class GreaterContext extends ComparatorContext {
		public GreaterContext(ComparatorContext ctx) { copyFrom(ctx); }
	}
	public static class LesserEqualContext extends ComparatorContext {
		public LesserEqualContext(ComparatorContext ctx) { copyFrom(ctx); }
	}

	public final ComparatorContext comparator() throws RecognitionException {
		ComparatorContext _localctx = new ComparatorContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_comparator);
		try {
			setState(161);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__22:
				_localctx = new GreaterContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(155);
				match(T__22);
				}
				break;
			case T__23:
				_localctx = new LesserContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				match(T__23);
				}
				break;
			case T__24:
				_localctx = new EqualContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(157);
				match(T__24);
				}
				break;
			case T__25:
				_localctx = new GreaterEqualContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(158);
				match(T__25);
				}
				break;
			case T__26:
				_localctx = new LesserEqualContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(159);
				match(T__26);
				}
				break;
			case T__27:
				_localctx = new NotEqualContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(160);
				match(T__27);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	 
		public ExpContext() { }
		public void copyFrom(ExpContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SubstractionContext extends ExpContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public SubstractionContext(ExpContext ctx) { copyFrom(ctx); }
	}
	public static class AdditionContext extends ExpContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public AdditionContext(ExpContext ctx) { copyFrom(ctx); }
	}
	public static class JustTermContext extends ExpContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public JustTermContext(ExpContext ctx) { copyFrom(ctx); }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_exp);
		try {
			setState(168);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				_localctx = new JustTermContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(163);
				term();
				}
				break;
			case 2:
				_localctx = new AdditionContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(164);
				match(T__28);
				setState(165);
				term();
				}
				break;
			case 3:
				_localctx = new SubstractionContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(166);
				match(T__29);
				setState(167);
				term();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	 
		public TermContext() { }
		public void copyFrom(TermContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MultiplicationContext extends TermContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public MultiplicationContext(TermContext ctx) { copyFrom(ctx); }
	}
	public static class ModuloContext extends TermContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public ModuloContext(TermContext ctx) { copyFrom(ctx); }
	}
	public static class DivisionContext extends TermContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public DivisionContext(TermContext ctx) { copyFrom(ctx); }
	}
	public static class JustFactorContext extends TermContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public JustFactorContext(TermContext ctx) { copyFrom(ctx); }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_term);
		try {
			setState(177);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__14:
			case T__15:
			case T__29:
			case T__33:
			case ID:
			case CONST_I:
			case CONST_F:
			case STRING:
				_localctx = new JustFactorContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(170);
				factor();
				}
				break;
			case T__30:
				_localctx = new MultiplicationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(171);
				match(T__30);
				setState(172);
				factor();
				}
				break;
			case T__31:
				_localctx = new DivisionContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(173);
				match(T__31);
				setState(174);
				factor();
				}
				break;
			case T__32:
				_localctx = new ModuloContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(175);
				match(T__32);
				setState(176);
				factor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class More_expressionsContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public More_expressionsContext more_expressions() {
			return getRuleContext(More_expressionsContext.class,0);
		}
		public More_expressionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_more_expressions; }
	}

	public final More_expressionsContext more_expressions() throws RecognitionException {
		More_expressionsContext _localctx = new More_expressionsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_more_expressions);
		try {
			setState(184);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(179);
				match(T__8);
				setState(180);
				expression(0);
				setState(181);
				more_expressions();
				}
				break;
			case T__2:
			case T__16:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public VarconstContext varconst() {
			return getRuleContext(VarconstContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode STRING() { return getToken(QuarkParser.STRING, 0); }
		public More_expressionsContext more_expressions() {
			return getRuleContext(More_expressionsContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_factor);
		int _la;
		try {
			setState(202);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__29:
			case ID:
			case CONST_I:
			case CONST_F:
				enterOuterAlt(_localctx, 1);
				{
				setState(187);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__29) {
					{
					setState(186);
					match(T__29);
					}
				}

				setState(189);
				varconst();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(190);
				match(T__1);
				setState(191);
				expression(0);
				setState(192);
				match(T__2);
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 3);
				{
				setState(194);
				match(T__14);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(195);
				match(STRING);
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 5);
				{
				setState(196);
				match(T__15);
				setState(197);
				expression(0);
				setState(198);
				more_expressions();
				setState(199);
				match(T__16);
				}
				break;
			case T__33:
				enterOuterAlt(_localctx, 6);
				{
				setState(201);
				match(T__33);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarconstContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(QuarkParser.ID, 0); }
		public TerminalNode CONST_I() { return getToken(QuarkParser.CONST_I, 0); }
		public TerminalNode CONST_F() { return getToken(QuarkParser.CONST_F, 0); }
		public VarconstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varconst; }
	}

	public final VarconstContext varconst() throws RecognitionException {
		VarconstContext _localctx = new VarconstContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_varconst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << CONST_I) | (1L << CONST_F))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			statement();
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__9) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__20) | (1L << T__21) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << ID) | (1L << TYPE_ID) | (1L << CONST_I) | (1L << CONST_F) | (1L << STRING))) != 0)) {
				{
				{
				setState(207);
				statement();
				}
				}
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_statement);
		try {
			setState(215);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(213);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(214);
				expression(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(QuarkParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public More_expressionsContext more_expressions() {
			return getRuleContext(More_expressionsContext.class,0);
		}
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(ID);
			setState(218);
			match(T__1);
			setState(219);
			expression(0);
			setState(220);
			more_expressions();
			setState(221);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TypeRuleContext typeRule() {
			return getRuleContext(TypeRuleContext.class,0);
		}
		public TerminalNode ID() { return getToken(QuarkParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			typeRule();
			setState(224);
			match(ID);
			setState(225);
			match(T__18);
			setState(226);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public ThingsContext things() {
			return getRuleContext(ThingsContext.class,0);
		}
		public MorethingsContext morethings() {
			return getRuleContext(MorethingsContext.class,0);
		}
		public TerminalNode EOF() { return getToken(QuarkParser.EOF, 0); }
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			things();
			setState(229);
			morethings();
			setState(230);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ThingsContext extends ParserRuleContext {
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TypedefContext typedef() {
			return getRuleContext(TypedefContext.class,0);
		}
		public ThingsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_things; }
	}

	public final ThingsContext things() throws RecognitionException {
		ThingsContext _localctx = new ThingsContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_things);
		try {
			setState(237);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				function();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(233);
				func_call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(234);
				assignment();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(235);
				expression(0);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(236);
				typedef();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MorethingsContext extends ParserRuleContext {
		public ThingsContext things() {
			return getRuleContext(ThingsContext.class,0);
		}
		public MorethingsContext morethings() {
			return getRuleContext(MorethingsContext.class,0);
		}
		public MorethingsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_morethings; }
	}

	public final MorethingsContext morethings() throws RecognitionException {
		MorethingsContext _localctx = new MorethingsContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_morethings);
		try {
			setState(243);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__9:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__17:
			case T__20:
			case T__21:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case ID:
			case TYPE_ID:
			case CONST_I:
			case CONST_F:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(239);
				things();
				setState(240);
				morethings();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*\u00f8\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2>\n\2\f\2\16\2A\13\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4R\n\4\3\5"+
		"\3\5\3\5\5\5W\n\5\3\6\3\6\3\6\5\6\\\n\6\3\6\3\6\5\6`\n\6\3\6\3\6\5\6d"+
		"\n\6\3\6\3\6\5\6h\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6p\n\6\3\7\3\7\3\7\3\7"+
		"\3\7\5\7w\n\7\3\b\3\b\3\b\3\b\7\b}\n\b\f\b\16\b\u0080\13\b\3\b\3\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0091\n\n\3\n\3\n"+
		"\3\n\3\n\7\n\u0097\n\n\f\n\16\n\u009a\13\n\3\13\3\13\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\5\f\u00a4\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00ab\n\r\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\5\16\u00b4\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00bb"+
		"\n\17\3\20\5\20\u00be\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\5\20\u00cd\n\20\3\21\3\21\3\22\3\22\7\22\u00d3\n"+
		"\22\f\22\16\22\u00d6\13\22\3\23\3\23\5\23\u00da\n\23\3\24\3\24\3\24\3"+
		"\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3"+
		"\27\3\27\3\27\5\27\u00f0\n\27\3\30\3\30\3\30\3\30\5\30\u00f6\n\30\3\30"+
		"\2\3\22\31\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\2\4\4\2\27"+
		"\30%%\4\2%%\'(\2\u010c\2\60\3\2\2\2\4G\3\2\2\2\6Q\3\2\2\2\bV\3\2\2\2\n"+
		"o\3\2\2\2\fq\3\2\2\2\16x\3\2\2\2\20\u0083\3\2\2\2\22\u0090\3\2\2\2\24"+
		"\u009b\3\2\2\2\26\u00a3\3\2\2\2\30\u00aa\3\2\2\2\32\u00b3\3\2\2\2\34\u00ba"+
		"\3\2\2\2\36\u00cc\3\2\2\2 \u00ce\3\2\2\2\"\u00d0\3\2\2\2$\u00d9\3\2\2"+
		"\2&\u00db\3\2\2\2(\u00e1\3\2\2\2*\u00e6\3\2\2\2,\u00ef\3\2\2\2.\u00f5"+
		"\3\2\2\2\60\61\7\3\2\2\61\62\7%\2\2\62\63\7\4\2\2\63\64\5\4\3\2\64\65"+
		"\7\5\2\2\65\66\7\6\2\2\66\67\5\n\6\2\67?\7\7\2\289\5\20\t\29:\7\7\2\2"+
		":;\5\"\22\2;<\7\b\2\2<>\3\2\2\2=8\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2"+
		"\2@B\3\2\2\2A?\3\2\2\2BC\7\t\2\2CD\5\"\22\2DE\7\b\2\2EF\7\b\2\2F\3\3\2"+
		"\2\2GH\7%\2\2HI\7\n\2\2IJ\5\n\6\2JK\5\6\4\2K\5\3\2\2\2LM\7\13\2\2MN\7"+
		"%\2\2NO\7\n\2\2OR\5\n\6\2PR\3\2\2\2QL\3\2\2\2QP\3\2\2\2R\7\3\2\2\2ST\7"+
		"\13\2\2TW\5\n\6\2UW\3\2\2\2VS\3\2\2\2VU\3\2\2\2W\t\3\2\2\2Xp\7&\2\2Y["+
		"\7\f\2\2Z\\\7\r\2\2[Z\3\2\2\2[\\\3\2\2\2\\p\3\2\2\2]_\7\16\2\2^`\7\r\2"+
		"\2_^\3\2\2\2_`\3\2\2\2`p\3\2\2\2ac\7\17\2\2bd\7\r\2\2cb\3\2\2\2cd\3\2"+
		"\2\2dp\3\2\2\2eg\7\20\2\2fh\7\r\2\2gf\3\2\2\2gh\3\2\2\2hp\3\2\2\2ip\7"+
		"\21\2\2jk\7\22\2\2kl\5\n\6\2lm\5\b\5\2mn\7\23\2\2np\3\2\2\2oX\3\2\2\2"+
		"oY\3\2\2\2o]\3\2\2\2oa\3\2\2\2oe\3\2\2\2oi\3\2\2\2oj\3\2\2\2p\13\3\2\2"+
		"\2qr\7\24\2\2rs\7&\2\2sv\7\25\2\2tw\5\n\6\2uw\5\16\b\2vt\3\2\2\2vu\3\2"+
		"\2\2w\r\3\2\2\2xy\7\4\2\2y~\5\n\6\2z{\7\26\2\2{}\5\n\6\2|z\3\2\2\2}\u0080"+
		"\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080~\3\2\2\2\u0081"+
		"\u0082\7\5\2\2\u0082\17\3\2\2\2\u0083\u0084\7\4\2\2\u0084\u0085\5\22\n"+
		"\2\u0085\u0086\5\34\17\2\u0086\u0087\7\5\2\2\u0087\21\3\2\2\2\u0088\u0089"+
		"\b\n\1\2\u0089\u0091\5\24\13\2\u008a\u008b\5\30\r\2\u008b\u008c\5\22\n"+
		"\7\u008c\u0091\3\2\2\2\u008d\u0091\5\30\r\2\u008e\u0091\7\21\2\2\u008f"+
		"\u0091\5&\24\2\u0090\u0088\3\2\2\2\u0090\u008a\3\2\2\2\u0090\u008d\3\2"+
		"\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091\u0098\3\2\2\2\u0092"+
		"\u0093\f\5\2\2\u0093\u0094\5\26\f\2\u0094\u0095\5\22\n\6\u0095\u0097\3"+
		"\2\2\2\u0096\u0092\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098"+
		"\u0099\3\2\2\2\u0099\23\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\t\2\2"+
		"\2\u009c\25\3\2\2\2\u009d\u00a4\7\31\2\2\u009e\u00a4\7\32\2\2\u009f\u00a4"+
		"\7\33\2\2\u00a0\u00a4\7\34\2\2\u00a1\u00a4\7\35\2\2\u00a2\u00a4\7\36\2"+
		"\2\u00a3\u009d\3\2\2\2\u00a3\u009e\3\2\2\2\u00a3\u009f\3\2\2\2\u00a3\u00a0"+
		"\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\27\3\2\2\2\u00a5"+
		"\u00ab\5\32\16\2\u00a6\u00a7\7\37\2\2\u00a7\u00ab\5\32\16\2\u00a8\u00a9"+
		"\7 \2\2\u00a9\u00ab\5\32\16\2\u00aa\u00a5\3\2\2\2\u00aa\u00a6\3\2\2\2"+
		"\u00aa\u00a8\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00b4\5\36\20\2\u00ad\u00ae"+
		"\7!\2\2\u00ae\u00b4\5\36\20\2\u00af\u00b0\7\"\2\2\u00b0\u00b4\5\36\20"+
		"\2\u00b1\u00b2\7#\2\2\u00b2\u00b4\5\36\20\2\u00b3\u00ac\3\2\2\2\u00b3"+
		"\u00ad\3\2\2\2\u00b3\u00af\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\33\3\2\2"+
		"\2\u00b5\u00b6\7\13\2\2\u00b6\u00b7\5\22\n\2\u00b7\u00b8\5\34\17\2\u00b8"+
		"\u00bb\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b5\3\2\2\2\u00ba\u00b9\3\2"+
		"\2\2\u00bb\35\3\2\2\2\u00bc\u00be\7 \2\2\u00bd\u00bc\3\2\2\2\u00bd\u00be"+
		"\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00cd\5 \21\2\u00c0\u00c1\7\4\2\2\u00c1"+
		"\u00c2\5\22\n\2\u00c2\u00c3\7\5\2\2\u00c3\u00cd\3\2\2\2\u00c4\u00cd\7"+
		"\21\2\2\u00c5\u00cd\7)\2\2\u00c6\u00c7\7\22\2\2\u00c7\u00c8\5\22\n\2\u00c8"+
		"\u00c9\5\34\17\2\u00c9\u00ca\7\23\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd"+
		"\7$\2\2\u00cc\u00bd\3\2\2\2\u00cc\u00c0\3\2\2\2\u00cc\u00c4\3\2\2\2\u00cc"+
		"\u00c5\3\2\2\2\u00cc\u00c6\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\37\3\2\2"+
		"\2\u00ce\u00cf\t\3\2\2\u00cf!\3\2\2\2\u00d0\u00d4\5$\23\2\u00d1\u00d3"+
		"\5$\23\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4"+
		"\u00d5\3\2\2\2\u00d5#\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00da\5(\25\2"+
		"\u00d8\u00da\5\22\n\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da%\3"+
		"\2\2\2\u00db\u00dc\7%\2\2\u00dc\u00dd\7\4\2\2\u00dd\u00de\5\22\n\2\u00de"+
		"\u00df\5\34\17\2\u00df\u00e0\7\5\2\2\u00e0\'\3\2\2\2\u00e1\u00e2\5\n\6"+
		"\2\u00e2\u00e3\7%\2\2\u00e3\u00e4\7\25\2\2\u00e4\u00e5\5\22\n\2\u00e5"+
		")\3\2\2\2\u00e6\u00e7\5,\27\2\u00e7\u00e8\5.\30\2\u00e8\u00e9\7\2\2\3"+
		"\u00e9+\3\2\2\2\u00ea\u00f0\5\2\2\2\u00eb\u00f0\5&\24\2\u00ec\u00f0\5"+
		"(\25\2\u00ed\u00f0\5\22\n\2\u00ee\u00f0\5\f\7\2\u00ef\u00ea\3\2\2\2\u00ef"+
		"\u00eb\3\2\2\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2"+
		"\2\2\u00f0-\3\2\2\2\u00f1\u00f2\5,\27\2\u00f2\u00f3\5.\30\2\u00f3\u00f6"+
		"\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f1\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6"+
		"/\3\2\2\2\30?QV[_cgov~\u0090\u0098\u00a3\u00aa\u00b3\u00ba\u00bd\u00cc"+
		"\u00d4\u00d9\u00ef\u00f5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}