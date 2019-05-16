--
-- PostgreSQL database dump
--

-- Dumped from database version 10.8 (Ubuntu 10.8-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.8 (Ubuntu 10.8-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: drivers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.drivers (
    driver_id integer NOT NULL,
    license integer,
    user_id integer
);


--
-- Name: drivers_driver_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.drivers_driver_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: drivers_driver_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.drivers_driver_id_seq OWNED BY public.drivers.driver_id;


--
-- Name: itineraries; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.itineraries (
    itinerary_id integer NOT NULL,
    date timestamp without time zone,
    start_time time without time zone,
    end_time time without time zone,
    driver_id integer,
    trolley_id integer,
    route_id integer
);


--
-- Name: itineraries_itinerary_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.itineraries_itinerary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: itineraries_itinerary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.itineraries_itinerary_id_seq OWNED BY public.itineraries.itinerary_id;


--
-- Name: routes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.routes (
    route_id integer NOT NULL,
    route_name character varying(25)
);


--
-- Name: routes_route_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.routes_route_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: routes_route_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.routes_route_id_seq OWNED BY public.routes.route_id;


--
-- Name: stops; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.stops (
    stop_id integer NOT NULL,
    stop_name character varying(25),
    latitude double precision,
    longitude double precision
);


--
-- Name: stops_stop_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.stops_stop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: stops_stop_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.stops_stop_id_seq OWNED BY public.stops.stop_id;


--
-- Name: stopsinroutes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.stopsinroutes (
    route_id integer NOT NULL,
    stop_id integer NOT NULL
);


--
-- Name: trolleys; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.trolleys (
    trolley_id integer NOT NULL,
    plate character varying(8),
    capacity integer,
    mileage double precision
);


--
-- Name: trolleys_trolley_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.trolleys_trolley_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: trolleys_trolley_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.trolleys_trolley_id_seq OWNED BY public.trolleys.trolley_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(30),
    password character varying(100),
    first_name character varying(30),
    last_name character varying(30),
    phone character(12),
    admin boolean
);


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: drivers driver_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.drivers ALTER COLUMN driver_id SET DEFAULT nextval('public.drivers_driver_id_seq'::regclass);


--
-- Name: itineraries itinerary_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itineraries ALTER COLUMN itinerary_id SET DEFAULT nextval('public.itineraries_itinerary_id_seq'::regclass);


--
-- Name: routes route_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.routes ALTER COLUMN route_id SET DEFAULT nextval('public.routes_route_id_seq'::regclass);


--
-- Name: stops stop_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.stops ALTER COLUMN stop_id SET DEFAULT nextval('public.stops_stop_id_seq'::regclass);


--
-- Name: trolleys trolley_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.trolleys ALTER COLUMN trolley_id SET DEFAULT nextval('public.trolleys_trolley_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: drivers; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.drivers (driver_id, license, user_id) FROM stdin;
1	6523034	1
2	1234567	3
3	8912345	4
\.


--
-- Data for Name: itineraries; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.itineraries (itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id) FROM stdin;
2	2019-05-17 00:00:00	08:00:00	11:00:00	1	1	1
3	2019-05-17 00:00:00	12:00:00	18:00:00	2	6	1
\.


--
-- Data for Name: routes; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.routes (route_id, route_name) FROM stdin;
1	Dummy Route #1
2	Dummy Route #2
3	Dummy Route #3
\.


--
-- Data for Name: stops; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.stops (stop_id, stop_name, latitude, longitude) FROM stdin;
1	Zoologico	18.2156651246421148	-67.1336746215820455
2	Biologia	18.2118739652150659	-67.138330936431899
3	Fisica	18.2108599179901276	-67.139629125595107
4	Patio Central	18.2112624801580374	-67.1408468484878682
\.


--
-- Data for Name: stopsinroutes; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.stopsinroutes (route_id, stop_id) FROM stdin;
1	1
1	2
1	3
2	1
2	2
3	4
3	3
3	2
\.


--
-- Data for Name: trolleys; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.trolleys (trolley_id, plate, capacity, mileage) FROM stdin;
1	GFN091	24	60000
2	ASL045	32	60000
6	PLS679	26	15000
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (user_id, username, password, first_name, last_name, phone, admin) FROM stdin;
1	jdcuevas	$5$rounds=535000$G.LAvioUkBoxQREk$pQmUUHG.y9NcCbXD5BsF/TZ/XhAbad6cMYMuSNqX0O.	Julian	Cuevas	787-607-4677	f
2	admin	$5$rounds=535000$RSPoIduwEUO8Ubmk$7W9WKs7Dg/tz5CciqkvCM6Qzf/qsZj6t2rWXdIiHnxD	admin	admin	999-999-9999	t
3	jdoe	$5$rounds=535000$LM6vaJ13TnagjJIY$J65wPOQEC4uiGc5NtOhdxpcuR5vHhUCNzwlXMiSt./C	John	Doe	666-666-6666	f
4	janed	$5$rounds=535000$zoQw1Qlpq5U4JBM3$8oekVEDs9f1GLXZ4igVJHWtYzEzXONW4xeLY7eWCUw/	Jane	Doe	777-777-7777	f
\.


--
-- Name: drivers_driver_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.drivers_driver_id_seq', 3, true);


--
-- Name: itineraries_itinerary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.itineraries_itinerary_id_seq', 3, true);


--
-- Name: routes_route_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.routes_route_id_seq', 3, true);


--
-- Name: stops_stop_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.stops_stop_id_seq', 4, true);


--
-- Name: trolleys_trolley_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.trolleys_trolley_id_seq', 6, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_user_id_seq', 4, true);


--
-- Name: drivers drivers_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.drivers
    ADD CONSTRAINT drivers_pkey PRIMARY KEY (driver_id);


--
-- Name: itineraries itineraries_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itineraries
    ADD CONSTRAINT itineraries_pkey PRIMARY KEY (itinerary_id);


--
-- Name: routes routes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.routes
    ADD CONSTRAINT routes_pkey PRIMARY KEY (route_id);


--
-- Name: stops stops_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.stops
    ADD CONSTRAINT stops_pkey PRIMARY KEY (stop_id);


--
-- Name: stopsinroutes stopsinroutes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.stopsinroutes
    ADD CONSTRAINT stopsinroutes_pkey PRIMARY KEY (route_id, stop_id);


--
-- Name: trolleys trolleys_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.trolleys
    ADD CONSTRAINT trolleys_pkey PRIMARY KEY (trolley_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: drivers drivers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.drivers
    ADD CONSTRAINT drivers_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: itineraries itineraries_driver_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itineraries
    ADD CONSTRAINT itineraries_driver_id_fkey FOREIGN KEY (driver_id) REFERENCES public.drivers(driver_id);


--
-- Name: itineraries itineraries_route_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itineraries
    ADD CONSTRAINT itineraries_route_id_fkey FOREIGN KEY (route_id) REFERENCES public.routes(route_id);


--
-- Name: itineraries itineraries_trolley_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itineraries
    ADD CONSTRAINT itineraries_trolley_id_fkey FOREIGN KEY (trolley_id) REFERENCES public.trolleys(trolley_id);


--
-- Name: stopsinroutes stopsinroutes_route_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.stopsinroutes
    ADD CONSTRAINT stopsinroutes_route_id_fkey FOREIGN KEY (route_id) REFERENCES public.routes(route_id);


--
-- Name: stopsinroutes stopsinroutes_stop_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.stopsinroutes
    ADD CONSTRAINT stopsinroutes_stop_id_fkey FOREIGN KEY (stop_id) REFERENCES public.stops(stop_id);


--
-- PostgreSQL database dump complete
--

