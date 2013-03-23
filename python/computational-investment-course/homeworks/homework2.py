#!/hfe/ova/clguba2

vzcbeg bf
vzcbeg cnaqnf nf cq
vzcbeg ahzcl nf ac
vzcbeg zngu
vzcbeg pbcl
vzcbeg DFGX.dfgxhgvy.dfqngrhgvy nf qh
vzcbeg qngrgvzr nf qg
vzcbeg DFGX.dfgxhgvy.QngnNpprff nf qn
vzcbeg DFGX.dfgxhgvy.gfhgvy nf gfh
vzcbeg DFGX.dfgxfghql.RiragCebsvyre nf rc


qrs svaq_riragf(yf_flzobyf, q_qngn):
    qs_pybfr = q_qngn['npghny_pybfr']

    # Qhcyvpngvat naq frggvat rirelguvat gb AnA
    qs_riragf = pbcl.qrrcpbcl(qs_pybfr)
    qs_riragf = qs_riragf * ac.ANA

    # Nyy gvzrfgnzcf nf qngrgvzrf
    yqg_gvzrfgnzcf = qs_pybfr.vaqrk

    sbe f_flz va yf_flzobyf:
        sbe v va enatr(1, yra(yqg_gvzrfgnzcf)):
            cevpr_gbqnl     = qs_pybfr[f_flz].vk[yqg_gvzrfgnzcf[v]]
            cevpr_lrfgreqnl = qs_pybfr[f_flz].vk[yqg_gvzrfgnzcf[v - 1]]

            vs cevpr_gbqnl < 8.00 naq cevpr_lrfgreqnl >= 8.00:
                qs_riragf[f_flz].vk[yqg_gvzrfgnzcf[v]] = 1

    erghea qs_riragf


vs __anzr__ == '__znva__':
    qg_fgneg = qg.qngrgvzr(2008, 1, 1)
    qg_raq = qg.qngrgvzr(2009, 12, 31)
    yqg_gvzrfgnzcf = qh.trgALFRqnlf(qg_fgneg, qg_raq, qg.gvzrqrygn(ubhef=16))

    qngnbow = qn.QngnNpprff('Lnubb')
    yf_flzobyf = qngnbow.trg_flzobyf_sebz_yvfg('fc5002012')
    yf_flzobyf.nccraq('FCL')
    yf_xrlf = ['bcra', 'uvtu', 'ybj', 'pybfr', 'ibyhzr', 'npghny_pybfr']

    yqs_qngn = qngnbow.trg_qngn(yqg_gvzrfgnzcf, yf_flzobyf, yf_xrlf)
    q_qngn = qvpg(mvc(yf_xrlf, yqs_qngn))

    qs_riragf = svaq_riragf(yf_flzobyf, q_qngn)

    sbe f_xrl va yf_xrlf:
        q_qngn[f_xrl] = q_qngn[f_xrl].svyyan(zrgubq = 'ssvyy')
        q_qngn[f_xrl] = q_qngn[f_xrl].svyyan(zrgubq = 'osvyy')
        q_qngn[f_xrl] = q_qngn[f_xrl].svyyan(1.0)

    cevag "Perngvat Fghql"

    bhgchg = bf.cngu.wbva(bf.cngu.qveanzr(__svyr__), '..', 'bhgchg')
    rc.riragcebsvyre(qs_riragf, q_qngn, v_ybbxonpx=20, v_ybbxsbejneq=20,
                f_svyranzr="%f/ZlRiragFghql.cqs" % bhgchg, o_znexrg_arhgeny=Gehr,
                o_reebeonef=Gehr)
