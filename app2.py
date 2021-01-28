import requests
import ast
import random

# load 3 chars
tl = """
u3o,3jn,x6n,6zf,w7o,w6t,3kp,7cg,g3w,u0t,f7w,6qv,kq0,73o,u3b,7rd,6xz,y0i,7qd,6e0,vnv,v6f,6r3,0lp,3ur,60b,f6g,0oy,0fw,6u0,70v,e0a,6hc,p0u,z0h,7fi,fu6,3ob,eyh,7yf,7zi,0qx,0el,f7x,x7k,x0q,vk3,bj6,q36,0nb,nb6,x7a,qf0,67j,e3x,um6,7ku,y6c,u3m,q7a,3vw,3ln,7vc,6ql,u0s,6hp,7uk,3qe,vy0,t6w,0jt,07g,j76,un7,o7y,36a,b3q,3np,any,76i,bzb,0gg,3uf,3ir,w6q,ay7,7p0,rre,0d6,7aq,6ig,7rh,37u,7qk,za6,03g,6zk,3lj,c6k,3m6,6ny,n3j,3mz,3ls,0fl,7fz,h6g,w7x,7fh,7cp,u7i,u0f,3fj,ru6,g6i,3ib,o7i,y6r,7hb,f6e,qs7,qn3,6gn,v7u,q7p,0rp,6yl,xxt,o7u,l6x,7l6,w7z,r7u,o7p,0k7,y6p,0x7,f7i,0je,6h0,6jy,6wi,xg6,7bn,7ct,3ih,q7u,cqw,y3o,0rl,x6i,3g6,zd7,c6f,7uj,wn6,u7y,g6y,7c3,qn7,3ql,o0b,6zg,0yf,6kc,0ql,7jb,6wf,b6q,l67,6jt,7je,nl7,i6k,w7i,367,73z,pq7,w6r,0fk,vw3,6kd,c6i,iuu,z7h,70t,0wk,p6s,7rq,u3z,0jk,7fd,6al,g7i,6pn,0l7,6wq,uqy,6xa,3qd,0qd,q0c,63b,o7j,6vi,i6h,ox6,q0v,7u3,w3u,3tg,3oa,06j,t7p,q7x,6ez,73f,0jg,06f,0ew,z6y,zf3,3yw,6da,7nr,6d0,h6b,6rq,q7g,03d,0uj,w6o,r7f,3hk,6t6,6bl,7hh,q7r,0zq,3yq,3l7,06u,0f3,3xq,en6,z6u,6un,7tc,0gs,a0y,i0o,f6u,3qk,qe7,y7f,ik3,0c6,6zx,7jy,r3j,3zc,0bo,7g0,l0h,7zh,63j,0u3,6pd,lq7,06s,6es,3b0,u7o,3sw,h7a,a6g,0bl,ix7,3vf,j6w,6lb,g6l,7wy,0gv,z0b,z7m,qad,0d7,j6j,7yr,k6d,7zj,6p0,0cc,e7r,s6l,6ds,q3g,0hb,6i3,3gc,6ki,g7u,x3b,q0u,0ww,wiq,p7e,0p3,ezj,6qk,ev6,p6e,h73,fq0,yt6,73j,y3u,ue6,03j,0tv,x6v,6jb,h7n,63q,3xn,0yk,0qg,7lr,0kx,suw,u0k,6pf,d6f,6xu,7xa,bmq,r6k,y7w,6va,7bd,r0u,7jm,y6o,6fr,76n,i7g,l6i,6mq,e6q,3tm,n6z,6lj,63g,6gp,s7b,dql,yp0,6xv,t7f,6pe,p6z,qo3,v6z,3cj,fh7,6gt,vu6,h6u,q63,w7v,u7e,s6p,6hu,70q,3bg,6vk,0c3,6jf,v6l,7hk,3uv,7zo,7n6,6zp,0mx,6ij,b6u,6uc,n6u,i6y,0iv,0fr,3hw,7pz,o3c,6qn,0gu,eo6,w6z,6ws,6ai,6qz,w6b,b0l,60p,uf7,q7s,y7t,hx3,3yf,e6p,7fw,70r,7hy,x6e,m7p,oj6,q7f,07p,y7l,0qi,k6q,wf3,7fj,63o,nv6,6ia,6c0,6q0,0w7,6dt,7lf,7jr,6k0,7xq,6bs,6ht,7nj,0yr,0tu,iw7,naq,63f,b7p,o7l,66j,0qr,k7w,cu6,3j0,7j3,gq3,f6b,6tj,u6p,0e7,u3e,0vj,q7v,vz6,6jd,u6h,w0i,q6f,iy6,a0j,6xc,p6h,37q,i6c,wr6,r6m,67x,3fw,tqo,7cq,f7v,g6u,0ph,0qs,6uq,n6r,663,3rz,v6h,6wc,t7j,j7t,0wd,l6a,03y,6pq,6bg,3ut,7fs,nf7,60o,y7j,u6i,api,7ht,0vx,7k3,76f,fo7,7z3,67w,l6o,p6t,v7g,i7l,t6k,c67,03l,7qc,6eq,e0q,ahq,67c,3vq,6z3,6jh,6gy,3fb,3gw,v0h,bh3,0ns,i6j,k6w,x3j,t6l,0lg,w6s,0mf,l6p,i6s,6v3,6fe,l7o,6rw,7r3,p6l,ej6,xk7,6yr,7wt,ot6,7iy,o6r,ql6,6y3,w6i,6ek,0hc,0v6,3uo,0ku,0wy,j7h,3jq,6uv,6wm,o3g,7sv,p6v,f7m,gn7,7bx,3fh,3m7,wr0,6bu,6ls,gv7,0oe,6wb,i6l,p6f,0ed,0nj,u6q,l7u,oxl,7av,v6y,l06,n7y,l6y,pn3,7g7,x7r,faj,h6d,6pl,iu3,7xg,6xq,0a3,u7j,i0e,hf6,i6a,vav,7mw,6pj,b0p,i6w,7fp,6sk,67o,fu0,7wk,q6w,0bk,3i6,efq,l7f,3ik,y7e,6e3,v6j,6vz,j0v,7pg,y70,qv7,7gz,6cj,uyy,6my,f6i,03u,r0f,l6s,k6x,3cn,tr3,k7b,0ay,k7j,6nw,u6o,3cv,7vp,6ga,3vp,q0d,u6x,6sb,nit,7vt,7jt,7bg,6eo,c3u,o7g,uau,73v,7si,ul0,sfv,6zj,0gx,i6v,6dr,wz7,vqk,3fq,n63,u0y,7oj,0rn,7ir,0ih,3l6,t6r,vzz,ie3,6of,3ff,u7c,uk6,0zd,z6r,lpo,0ir,0oa,7ah,6ho,7ta,7b6,p6u,6kx,ze7,s7m,g6v,6ro,q6s,70w,6hh,l6g,6sr,g6j,om6,qkj,3kj,6vr,7ju,a0p,0fi,hk0,qv6,k6v,a0i,7gj,hl6,6c7,0uc,6ol,wn3,nq6,7b0,y6u,0vc,vhw,3vu,3zg,q0l,63d,p7x,7lz,yb6,b7l,j7o,0ft,qfg,3a0,06e,7tu,03v,h66,6jx,76o,q7i,qq6,6hl,e0o,ow3,0jz,6ly,7bh,6vq,6nq,7e6,0ie,0bv,0yd,6hm,q7d,izl,x6r,6cx,3qg,7cv,u0j,o0m,6qg,6ud,w7u,6xb,0yv,ueu,73g,zdq,qd6,h7t,7l3,7of,ch6,j7k,6kr,3s6,6gd,7dy,c6j,7jf,63a,o7b,n7b,o7e,7i6,3jt,h6y,6np,0eb,m6f,n7t,j7f,0qn,6cw,07r,bkk,6cf,7vq,3z6,q6y,vy6,7nn,0vf,m7t,iq6,tf7,6bh,6vn,6ep,6wn,z3q,67u,d6v,g0j,l6t,6gi,3n6,d7w,6bj,0fb,7zs,3yb,q0f,3fl,u3a,3zi,7zq,0n7,q0h,i7q,ew7,0kf,t6q,6j0,3vh,6dw,0ig,3uj,3bw,u36,7em,6md,6hv,0wb,b7c,6gm,v0g,6eg,d6x,77v,lk7,7yy,0ug,7uo,6ih,au3,0lt,07j,uj7,07t,kz6,q7b,n6e,qs6,c6m,y6h,jxq,wc6,6pw,vf7,7i0,c6o,0vn,6ww,l0q,6bd,3qn,6yo,v6n,e0j,7ra,7ax,jo6,0tc,q7e,6tw,7pl,l7a,o6u,q3v,ei6,a6f,we0,60f,7wi,j6c,76d,0an,dd7,g3y,7a3,6o0,6w0,0qv,7wg,0nh,jiz,u0e,z6h,7yk,f3o,0cu,7xu,h7b,3by,q3b,zvt,6ej,p3y,o0u,g7j,6tz,0kb,w7b,7jz,6dv,nq3,na6,6rn,wg3,6i7,y67,ouu,n6f,6t0,6mu,3sz,0b3,mj7,u0d,s0k,363,30v,7jw,0kw,u0r,7uw,7g6,7vh,6i0,n6b,6vg,30e,7tl,7hq,s3q,7f3,zv7,6vj,e6f,0jy,0vg,e3u,6j7,e0y,0eh,6be,0eq,7ei,hv6,uz6,wd6,u7t,06g,i7p,f7t,m7l,z6c,3oq,f3v,f7z,l7w,77r,m6y,yw3,p6k,v6c,7pu,0wj,60l,6fs,wek,s6j,7r6,7aw,3zq,3zj,6ic,6m3,7m0,e7b,7u0,gq6,f0a,3te,63z,a6v,0gy,6iz,0yo,f3u,t3u,7qf,7j6,66p,76m,6rh,7ej,3gk,6ul,q3e,yvq,0dl,3eq,0bq,l7i,73d,i6x,un6,q7z,6sy,u7q,3ey,v6u,ug6,7ha,6pc,7gp,h0r,0g6,r7i,qc6,7nm,7rp,e7z,0gj,3qz,ux6,07q,3l0,p66,xj3,6em,7yl,6ip,0jn,0vt,0gb,7qq,0hv,0f6,0t6,3q0,0yb,3e6,c6q,0nq,7dp,zwi,7qt,7eb,3cf,6oa,7my,d7j,3oj,ve0,0oj,7ee,v7h,y7y,x6g,6py,6kl,3jm,6fw,0j7,q6i,3pz,06l,u7u,q0o,6ok,3wy,b6f,6aq,y0v,6q3,6wo,y63,6so,bq6,6he,7ve,0ag,y6n,07w,7tg,j7g,6bo,0bg,d0a,z0w,7yw,7fb,6cn,p6r,6yz,7k0,g7n,vf3,j7v,fp6,e6n,6lr,q0j,i6b,u3w,7p6,i0j,s0q,03f,6nj,0fq,76u,6hf,ll3,0pe,7zr,nl6,7hx,vs6,60u,0oq,u3t,6iy,d6q,0uy,qcb,73u,i7t,7qo,6n0,s6y,0pv,6ni,aq0,q7n,7gk,sq6,6l3,7nh,i3y,g7l,u0q,0s6,7lw,3pb,vfj,0z3,7la,7xd,36y,6mj,6xj,ey0,6xt,6bm,6fk,q6b,63e,x7g,3oy,6zd,6oe,o3f,j7z,0ik,e7h,7lq,x6w,d7u,6tp,p6y,o6h,0zu,7b3,60i,0td,36x,7xt,7iw,7yz,u3i,ib6,3z7,x36,76w,i6n,p6o,6g0,0cf,77u,7ud,q6x,6tr,0u7,ms7,cla,zt6,06w,r6f,07f,0fn,bz7,7yh,7yd,unw,g6m,xg7,7vd,3hx,7sq,3k6,6yw,6au,n6p,3zl,7pf,j7c,0nt,6qp,3jv,63x,v0p,y7v,xvl,g6q,70l,qj6,3zx,u3p,z6b,j0q,6l7,6tl,0s3,e6z,3h7,qk7,73s,7ur,7mo,uub,nt0,x6l,oh7,0qe,u6g,0yl,ty3,6a0,h7v,iei,t6j,66r,q0g,qp6,t0a,t6i,06p,06i,6hi,evb,e6o,67t,0lv,763,0bn,yp6,x6k,p7n,3pg,u7p,7kh,0ub,70h,v6b,3r6,0zn,3ua,0ob,6fi,7bc,v6q,w0a,i7n,0wf,r3w,6ha,63s,7f0,0sd,3j6,e6w,0lx,6b0,7gh,gq7,nhj,7i3,06t,yq6,h6f,7wx,6zl,j00,03o,0bz,60g,6yd,wn7,o6p,6gc,73i,37g,6yc,6sz,ny7,0cj,g3u,6pg,6as,n7e,6hb,7pj,7g3,67s,3uy,q0n,z6q,3bj,6lx,0hx,7v6,i7h,33u,7t3,y6e,zq0,7wr,06a,q3d,n6y,7ec,6oh,7ub,36w,6gz,zzv,6nk,rq6,7y0,6gv,7bo,w6y,7lx,w7y,3rv,qg3,h7l,0ea,6ot,3o7,j7w,0ow,3wl,3yt,6sq,l7c,0ln,7dv,a7u,7mq,fo6,6rv,k6m,6om,o03,pr6,f6d,6el,6rm,6jz,e7v,w6j,uw6,3yd,7lh,7gy,w76,kw0,7xj,r6n,6p7,7w6,3us,o3t,yv3,3bq,6tx,6wt,7qn,t0l,n6i,07n,3wn,qmj,fy7,73l,cc6,6j3,p3j,6b3,30i,vv7,6ct,q3z,q0x,q3j,3a6,u06,f7j,vqz,6lg,u7w,7ig,6qq,q6e,v6a,6pv,iro,6um,0yp,7xb,k6z,j6q,p6d,0sp,t6f,q6j,6z6,07c,6cq,7ja,0eg,vf6,uq6,duh,6bi,y6q,6zv,v3u,weu,7nx,3w7,7cu,il6,6cd,6fm,s33,0j3,66q,yw6,vqj,f0q,w60,0sx,oia,0n6,7rw,6lf,6nn,g6h,0nc,3gx,0vw,eq7,m6h,z6a,tl6,0yt,s6g,e3h,o0s,yd0,z0a,7rs,3xu,s0z,3pv,7qm,7wq,03c,7wa,3uc,0vq,7ij,0gw,6cs,0zp,6qa,6qo,d6k,0vb,6sl,wev,i0v,ft7,f6w,e7n,v3v,0vs,z6o,i6t,vq7,k3j,0lr,qfv,6qe,k7t,t6v,63t,3qr,qy0,u6e,03p,07e,7bv,0ov,0wv,07v,6k3,3hq,7ua,0w6,ay6,co0,6s0,0hd,qil,o0j,0p7,kei,70i,0lf,3xf,7xv,g66,i0a,ny6,67d,76p,6ov,p7l,0gr,76j,3u6,x3x,7xf,0fc,v06,37y,e7w,6r7,w6p,30f,t7d,3gl,3b6,0va,jq6,bz6,6xf,j6u,6nr,3t6,i3h,jkt,7ln,3f7,a6d,i3r,6yx,6hy,7pr,6t3,vv0,0sg,3hu,0tq,0wg,3gj,7lo,0h7,7dn,7sz,man,6fn,3ah,7tj,7zf,0fh,3jx,7qz,3qw,u76,or6,h6z,6pp,6fy,c7b,7lj,3h6,0lq,w0p,3lc,h7q,f0m,3mf,0cl,x6z,u6l,0vh,6bn,o7w,0dw,6bw,3yv,y6z,g0i,i0g,r6g,6nd,7vy,v7f,06k,n6d,3tv,0q7,d6j,0wx,77n,7jq,6a7,067,73c,f6l,vo6,06n,qje,o6q,0tp,0zm,h6v,cq0,hq3,b7x,7zv,73y,7yn,0ua,6tc,r6e,6ee,3uq,7h0,0rq,q7y,7jg,o0g,6fo,xnn,hff,0cy,7rf,c6x,pu7,3td,0od,p0a,uo0,6ym,n7q,b6i,36m,6kt,6k7,7gq,l6f,qz6,iy3,7qj,3fu,3rj,zu6,0lw,n7o,3yr,0dq,7vw,wu6,r6z,b0v,w0g,gn6,p6i,v63,7ww,a0w,3o6,y6d,37l,7kv,3wx,y7b,6uo,c6d,ul7,e6g,za7,o0k,6ua,u0c,yta,q6k,0hk,3iw,6dp,6vy,0f7,6uf,a03,0fv,e7j,3ou,q3i,7mv,d6l,u6m,ii6,0mb,7nw,e6i,sv6,fk6,3qt,0yw,u0z,7nf,zf6,6ln,r3h,6gl,6se,qr0,0fz,v7j,r6q,v7d,6nh,idv,fu3,0j6,xoy,7h6,6mp,7w3,7uh,e3f,f6t,6fj,7ts,7dx,67l,3kw,3aj,0b6,7xh,70p,p3o,qy6,6xp,7yj,0cv,ez7,i0w,7nu,0em,o6g,7we,3zv,6gf,n6l,60x,6sn,mj3,e6m,m7q,j36,6vw,uh0,7q0,0ot,6cp,t6y,6xk,o67,7lg,6jo,0kv,7yx,6st,7is,07y,76h,yv6,0q6,7wo,pw7,6q6,0p6,7mn,3nq,6bf,h6j,6jm,t7w,7dg,3fo,eie,6wp,3qh,0b7,60q,6nx,63h,637,i6p,6qt,7vi,06x,6hn,q6h,0df,6gs,6ty,rja,6go,ix6,3y7,fb7,kq6,6fz,iy7,t7o,q0i,eii,u6y,0ei,3og,3ov,c6b,g0u,6re,0qu,0ic,6jn,0if,6bp,3f0,z6i,0r6,6pu,xb7,60n,7oe,0qz,u6d,6sf,7qw,7uv,6le,7zu,3so,x6c,7lp,6at,6wg,mxq,6ou,6jv,6eb,w6v,7tn,3cl,3hb,3qv,6bv,j6h,y6i,y7c,u3j,0k6,37t,6cr,6f3,6af,v0k,u6t,6dz,6jj,7vm,6lq,30o,f6h,7v0,3nw,p6q
"""

result = [x.strip() for x in tl.split(",")]


def randy():
    random.seed()
    random.shuffle(result)
    return result[random.randint(0, 1000)]


headers = {
    "date": "Thu, 28 Jan 2021 10:58:24 GMT",
    "cache-control": "max-age=0, must-revalidate, no-cache, no-store, private",
    "expires": "Fri, 04 May 1984 22:15:00 GMT",
    "access": "application/vnd.protonmail.api+json;apiversion=3",
    "set-cookie": "Session-Id=YBKY0CPblci3pj9lcWfyJAAAAJs; Domain=protonmail.com; Path=/; HttpOnly; Secure; Max-Age=7776000, Version=default; Path=/; Secure; Max-Age=7776000",
    "content-length": "89",
    "content-type": "application/json",
    "content-security-policy": "default-src 'self'; connect-src 'self' blob:; script-src 'self' blob: 'sha256-eAhF1Kdccp0BTXM6nMW7SYBdV0c3fZwzcC177TQ692g='; style-src 'self' 'unsafe-inline'; img-src http: https: data: blob: cid:; frame-src 'self' blob: https://secure.protonmail.com; object-src 'self' blob:; child-src 'self' data: blob:; report-uri https://reports.protonmail.ch/reports/csp; frame-ancestors 'none';",
    "strict-transport-security": "max-age=31536000; includeSubDomains; preload",
    "expect-ct": 'max-age=2592000, enforce, report-uri="https://reports.protonmail.ch/reports/tls"',
    "public-key-pins-report-only": 'pin-sha256="8joiNBdqaYiQpKskgtkJsqRxF7zN0C0aqfi8DacknnI="; pin-sha256="drtmcR2kFkM8qJClsuWgUzxgBkePfRCkRpqUesyDmeE="; report-uri="https://reports.protonmail.ch/reports/tls"',
    "x-frame-options": "deny",
    "x-content-type-options": "nosniff",
    "x-xss-protection": "1; mode=block; report=https://reports.protonmail.ch/reports/csp",
    "referrer-policy": "strict-origin-when-cross-origin",
    "x-permitted-cross-domain-policies": "none",
    "onion-location": "https://protonirockerxow.onion",
    "x-pm-appversion": "Web_3.16.53",
    "x-pm-apiversion": "3",
}

taken = []
avail = []


def check():
    rand = randy()
    url = f"https://mail.protonmail.com/api/users/available?Name={rand}"
    r = requests.get(url, headers=headers)
    kek = ast.literal_eval(f"{r.text}")
    print(f"Checking {rand}  ...")
    if kek.get("Code") == 12106:
        print(f"Code 12106: Username {rand} already used")
        taken.append(f"{rand} taken")
    elif kek.get("Code") == 1000:
        print(f"Code 1000: Username {rand} avail")
        avail.append(f"{rand} avail")
    else:
        print("wat")


if __name__ == "__main__":
    while True:
        check()
        print(avail)
