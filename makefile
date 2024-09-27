.PHONY: rng primes miller solo

rng:
	@python3 -m rng.Report

primes:
	@python3 -m primes.Report

miller:
	@python3 -m primes.Miller

solo:
	@python3 -m primes.Solovay