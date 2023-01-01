# tlv

![Build status](https://github.com/priv-kweihmann/tlv/workflows/Build/badge.svg)
[![PyPI version](https://badge.fury.io/py/tlv.svg)](https://badge.fury.io/py/tlv)
[![Python version](https://img.shields.io/pypi/pyversions/tlv)](https://img.shields.io/pypi/pyversions/tlv)
[![Downloads](https://img.shields.io/pypi/dm/tlv)](https://img.shields.io/pypi/dm/tlv)

Too less variation - A tool to discover code duplication in various languages

## Purpose

Code duplication are hard to track across many files.
There are tools existing like [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) (from PMD) which are doing a great job, but they require JAVA (or even some more obscure language) to run.
So I decided to write a small tool which uses [Pygments](http://pygments.org/) and python [difflib](https://docs.python.org/3/library/difflib.html) to catch code duplications for as many languages as possible

## Requirements

* python3
* [Pygments](http://pygments.org/)

## Installation

### PyPi

simply run

```sh
pip3 install tlv
```

### From source

* Install the needed requirements by running ```pip3 install Pygments```
* git clone this repository
* cd to \<clone folder\>
* run ```sudo ./build.sh```

## Usage

```shell
usage: tlv [-h] [--minlines MINLINES] [--mintoken MINTOKEN] [-j JOBS]
           [--lexer {...}]
           [--wildcard_token {...}]
           [--verbose] [--nodetails]
           files [files ...]

Find code duplications across various languages
positional arguments:
  files                 Files to parse

optional arguments:
  -h, --help            show this help message and exit
  --minlines MINLINES   Minimum length of block in lines before reporting
  --mintoken MINTOKEN   Minimum length of block in token before reporting
  -j JOBS, --jobs JOBS  Number of jobs to run in parallel
  --lexer {3d,aap,actionscript,actionscript3,ada,ada2005,ada95,adl,agda,ahk,al,alloy,amienttalk,amienttalk/2,ampl,an,antlr,antlr-actionscript,antlr-as,antlr-c#,antlr-cpp,antlr-csharp,antlr-java,antlr-perl,antlr-python,antlr-r,antlr-ruy,apachecon,apl,applescript,arduino,arexx,as,as3,asemake,asic,asm,aspectj,aspx-cs,asy,asymptote,at,atch,augeas,autohotkey,autoit,awk,c,c#,c++,c++-ojdum,c-ojdump,ca65,cadl,camkes,capdl,capnp,casic,ceylon,chai,chaiscript,chapel,charmci,cheetah,chpl,cirru,cl,clay,clean,clj,cljs,clojure,clojurescript,cmake,cmas,co,code,common-lisp,componentpascal,console,control,cool,coq,cp,cpp,cpp-ojdump,cpsa,cr,crmsh,croc,cry,cryptol,crystal,csh,csharp,csound,csound-csd,csound-document,csound-orc,csound-sco,csound-score,css,css+django,css+er,css+genshi,css+genshitext,css+jinja,css+lasso,css+mako,css+mozpreproc,css+php,css+ruy,css+smarty,cu,cucumer,cuda,cxx-ojdump,cypher,cython,d,d-ojdump,dart,dasm16,decontrol,delphi,desources,dg,di,django,do,docker,dosatch,doscon,dpatch,dtd,duy,dylan,dylan-console,dylan-lid,dylan-repl,e,earl-grey,earlgrey,easytrieve,ec,ecl,eg,ei,elisp,elixir,elm,emacs,emacs-lisp,en,er,erl,erlang,evoque,ex,exs,extempore,ezhil,gap,gas,gawk,genshi,genshitext,gherkin,glsl,gnuplot,go,golo,gooddata-cl,gosu,gro,groovy,gst,haml,handlears,haskell,haxe,haxeml,hexdump,hlsl,hs,hsa,hsail,hspec,html,html+cheetah,html+django,html+er,html+evoque,html+genshi,html+handlears,html+jinja,html+kid,html+lasso,html+mako,html+myghty,html+ng2,html+php,html+ruy,html+smarty,html+spit,html+twig,htmldjango,http,hx,hxml,hxsl,hylang,i,i6t,idl,idl4,idr,idris,iex,igor,igorpro,ik,in,ini,io,ioke,ir,irc,isaelle,itex,j,jade,jags,jasmin,jasminxt,java,javascript,javascript+cheetah,javascript+django,javascript+er,javascript+genshi,javascript+genshitext,javascript+jinja,javascript+lasso,javascript+mako,javascript+myghty,javascript+php,javascript+ruy,javascript+smarty,jcl,jinja,jl,jlcon,jproperties,js,js+cheetah,js+django,js+er,js+genshi,js+genshitext,js+jinja,js+lasso,js+mako,js+myghty,js+php,js+ruy,js+smarty,js+spit,jsg,json,json-ld,json-oject,jsonld,jsp,julia,juttle,kal,kcon,kid,koka,kotlin,lagda,lasso,lassoscript,lcry,lcryptol,lean,less,lhaskell,lhs,lid,lidr,lidris,lighttpd,lighty,limo,liquid,lisp,literate-agda,literate-cryptol,literate-haskell,literate-idris,litzasic,litzmax,live-script,livescript,llvm,logos,logtalk,lua,m2,make,make,mako,maql,mask,mason,mathematica,matla,matlasession,mawk,max,md,minid,mma,modelica,modula2,moin,monkey,monte,moo,moocode,moon,moonscript,mq4,mq5,mql,mql4,mql5,msc,mscgen,mupad,mxml,myghty,mysql,n,nasm,nawk,ncl,nesc,newlisp,newspeak,ng2,nginx,nim,nimrod,nit,nix,nixos,nn,nsh,nsi,nsis,numpy,nusmv,oa,ocaml,octave,odin,oj-c,oj-c++,oj-j,ojc,ojc++,ojdump,ojdump-nasm,ojective-c,ojective-c++,ojective-j,ojectivec,ojectivec++,ojectivej,ojectpascal,ojj,oo,ooc,oogie,opa,openedge,openugs,pacmancon,pan,parasail,pas,pascal,pawn,pcmk,perl,perl6,php,php3,php4,php5,pig,pike,pkgcon,pl,pl6,plpgsql,plus,po,posh,postgres,postgres-console,postgresql,postgresql-console,postscr,postscript,pot,pov,powershell,praat,progress,prolog,properties,protou,ps1,ps1con,psm1,psql,pug,puppet,py,py3,py3t,pycon,pypy,pypylog,pyrex,pyt,python,python3,pyx,qasic,qml,qs,qvt,qvto,r,racket,ragel,ragel-c,ragel-cpp,ragel-d,ragel-em,ragel-java,ragel-ojc,ragel-r,ragel-ruy,rain,raw,rcon,rd,red,red/system,redcode,registry,reol,resource,resourceundle,rexx,rhtml,rkt,rnc,rng-compact,ro,roocon,root,rql,rs,rsl,rts,rust,ruy,s,sage,salt,sarl,sas,sass,satch,sc,scala,scaml,scheme,scila,scm,scss,shell-session,silver,slash,slim,sls,slurm,smali,smalltalk,smarty,sml,snool,sources.list,sourceslist,sp,sparql,spec,spit,splus,sql,sqlite3,squeak,squidcon,st,st-pytex,stan,stata,supercollider,sv,swi,swig,systemverilog,t-sql,tads3,tap,tasm,tcl,tcsh,tcshcon,tea,teraterm,teratermmacro,termcap,termin,terra,thri,todotxt,toml,tra,trac-wiki,treetop,ts,tsql,ttl,turtle,twig,typescript,typoscript,typoscriptcssdata,typoscripthtmldata,ucode,ugs,unicon,uriscript,v.net,vala,vapi,vcl,vclsnippet,vclsnippets,vctreestatus,velocity,vgl,vhdl,vim,vnet,vscript,wdi,whiley,winatch,winugs,x10,xml,xml+cheetah,xml+django,xml+er,xml+evoque,xml+genshi,xml+jinja,xml+kid,xml+lasso,xml+mako,xml+myghty,xml+php,xml+ruy,xml+smarty,xml+spit,xorg,xq,xql,xqm,xquery,xqy,xten,xtend,yaml,yaml+jinja}
                        Manually set a lexer to use on all files
  --wildcard_token {Token.Keyword,Token.Keyword.Constant,Token.Keyword.Declaration,Token.Keyword.Namespace,Token.Keyword.Pseudo,Token.Keyword.Reserved,Token.Keyword.Type,Token.Name,Token.Name.Attribute,Token.Name.Builtin,Token.Name.Builtin.Pseudo,Token.Name.Class,Token.Name.Constant,Token.Name.Decorator,Token.Name.Entity,Token.Name.Exception,Token.Name.Function,Token.Name.Function.Magic,Token.Name.Label,Token.Name.Namespace,Token.Name.Other,Token.Name.Tag,Token.Name.Variable,Token.Name.Variable.Class,Token.Name.Variable.Global,Token.Name.Variable.Instance,Token.Name.Variable.Magic,Token.Literal,Token.Literal.Date,Token.Literal.String,Token.Literal.String.Affix,Token.Literal.String.Backtick,Token.Literal.String.Char,Token.Literal.String.Delimiter,Token.Literal.String.Doc,Token.Literal.String.Double,Token.Literal.String.Escape,Token.Literal.String.Heredoc,Token.Literal.String.Interpol,Token.Literal.String.Other,Token.Literal.String.Regex,Token.Literal.String.Single,Token.Literal.String.Symbol,Token.Literal.Number,Token.Literal.Number.Bin,Token.Literal.Number.Float,Token.Literal.Number.Hex,Token.Literal.Number.Integer,Token.Literal.Number.Integer.Long,Token.Literal.Number.Oct,Token.Operator,Token.Operator.Word,Token.Punctuation,Token.Comment,Token.Comment.Hashbang,Token.Comment.Multiline,Token.Comment.Preproc,Token.Comment.Single,Token.Comment.Special,Token.Generic,Token.Generic.Deleted,Token.Generic.Emph,Token.Generic.Error,Token.Generic.Heading,Token.Generic.Inserted,Token.Generic.Output,Token.Generic.Prompt,Token.Generic.Strong,Token.Generic.Subheading,Token.Generic.Traceback,Token.Text.Whitespace}
                        Token types that are threated as wildcards (actual
                        value doesn't matter)
  --verbose             Verbose output
  --nodetails           Dump the details of a finding
```

By default tool guesses the content type by the filename, if that doesn't work for you please see below

### Specify a lexer

You can use a specific lexer by running the tool with the **--lexer=** option.
When doing this all input files are processed by the specified lexer, you have to ensure that all passed files are of the specified file, else the results might be bogus.

## Output

Output will be written to stdout.
There are 2 possible finding types

* Duplicate - The code is exactly the same
* TooLessVariation - The code is the same, when removing all token types specified by --wildcard_token

### Output example

```shell
/someplace/busybox/modutils/modutils.c:9:0:[TooLessVariation]:Block till 16:0 is nearly the same as in ../modprobe-small.c from 29:0 till 36:0
>>> #include <sys/syscall.h>
>>> 
>>> #define init_module(mod, len, opts) syscall(__NR_init_module, mod, len, opts)
>>> #if defined(__NR_finit_module)
>>> # define finit_module(fd, uargs, flags) syscall(__NR_finit_module, fd, uargs, flags)
>>> #endif
>>> #define delete_module(mod, flags) syscall(__NR_delete_module, mod, flags)
>>> 
<<<
>>> #include <sys/syscall.h>
>>> 
>>> #define init_module(mod, len, opts) syscall(__NR_init_module, mod, len, opts)
>>> #define delete_module(mod, flags) syscall(__NR_delete_module, mod, flags)
>>> #ifdef __NR_finit_module
>>> # define finit_module(fd, uargs, flags) syscall(__NR_finit_module, fd, uargs, flags)
>>> #endif
>>> 
<<<
/someplace/busybox/modutils/modutils.c:165:32:[Duplicate]:Block till 169:3 is the same as in ../modprobe-small.c from 324:18 till 327:0
>>> 
>>> 	fstat(fd, &st);
>>> 	image = NULL;
>>> 	/* st.st_size is off_t, we can't just pass it to mmap */
>>> 	if
<<<
/someplace/busybox/modutils/modprobe-small.c:236:15:[Duplicate]:Block till 240:10 is the same as in ../modutils.c from 265:26 till 269:10
>>> 
>>> 	case ENOEXEC:
>>> 		return "invalid module format";
>>> 	case ENOENT:
>>> 		return "
<<<
/someplace/busybox/modutils/modutils.c:115:0:[Duplicate]:Block till 130:43 is the same as in ../modprobe-small.c from 177:0 till 194:36
>>> 
>>> #if ENABLE_FEATURE_CMDLINE_MODULE_OPTIONS
>>> char* FAST_FUNC parse_cmdline_module_options(char **argv, int quote_spaces)
>>> {
>>> 	char *options;
>>> 	int optlen;
>>> 
>>> 	options = xzalloc(1);
>>> 	optlen = 0;
>>> 	while (*++argv) {
>>> 		const char *fmt;
>>> 		const char *var;
>>> 		const char *val;
>>> 
>>> 		var = *argv;
>>> 		options = xrealloc(options, optlen + 2 + 
<<<
```

if you don't want to see the code itself, pass the **--nodetails** option

## Further reading

* [Pygments](http://pygments.org/)

## Bugs & Contribution

Feel free to create issues or pull requests
