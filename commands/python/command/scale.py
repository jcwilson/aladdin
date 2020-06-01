#!/usr/bin/env python3
from arg_tools import add_namespace_argument
from libs.k8s.kubernetes import Kubernetes
import logging


def parse_args(sub_parser):
    subparser = sub_parser.add_parser("scale", help="Scale a deployment to n replicas")
    add_namespace_argument(subparser)
    subparser.add_argument("deployment", help="which deployment to scale")
    subparser.add_argument("replicas", type=int, help="how many replicas to scale to")
    subparser.set_defaults(func=scale_args)


def scale_args(args):
    scale(args.deployment, args.replicas, args.namespace)


def scale(deployment, replicas, namespace=None):
    k = Kubernetes(namespace=namespace)

    k.scale(deployment, replicas)
    logging.info(
        "Scaled {deployment} to {replicas} replicas".format(
            deployment=deployment, replicas=replicas
        )
    )
