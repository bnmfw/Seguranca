.PHONY: rng dispute primes miller solo

rng:
	@python3 -m rng.Report

primes:
	@python3 -m primes.Report

dispute:
	@python3 -m primes.Dispute

miller:
	@python3 -m primes.Miller

solo:
	@python3 -m primes.Solovay